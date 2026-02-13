import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import log10, floor, ceil

from exp_data import ExpData
from util import splitIsotope
from util import periodicTable
from mass_table import getMassTable

from config import colors, markers, PATH_TO_HIVAPS

warnings.filterwarnings("ignore")

plt.rcParams.update({"font.size": 18})

periodicTable = periodicTable()

class Reaction:
    def __init__(
        self,
        projectile,
        target,
        cn,
        barfac,
        sigr,
        V0,
        R0,
        energy_values="beam", #"beam" or "exc" for excitation energy
        unit="mb",
        m_proj=1,
        m_targ=1,
        m_cn=1,
        evap_channel="xn",
        bf_diff=0.00,
        plot_diff=True,
        channels_to_plot=[],
        lowYRange=0,
        highYRange=0,
        lowXRange=0,
        highXRange=0,
        exp_data: ExpData = None,
        plot_exp_data=True,
        convert_exp_data=False,
        plot_maxCS_data=False,
        show_bass_barrier=False,
        reaction_info_note="",
        save_note="",
    ):
        self.projectile = projectile
        self.target = target
        self.cn = cn
        self.barfac = barfac
        if unit not in ["mb", "ub", "nb", "pb"]:
            raise ValueError("Invalid cross section unit")
        self.unit = unit
        self.evap_channel = evap_channel
        self.sigr = sigr
        self.V0 = V0
        self.R0 = R0
        self.energy_values = energy_values
        self.bf_diff = bf_diff
        self.plot_diff = plot_diff
        self.data_ifus0, self.data_ifus10 = None, None
        (
            self.data_ifus0_bf_low,
            self.data_ifus0_bf_high,
            self.data_ifus10_bf_low,
            self.data_ifus10_bf_high,
        ) = (None, None, None, None)
        self.channels_to_plot = channels_to_plot
        self.lowYRange = lowYRange
        self.highYRange = highYRange
        self.lowXRange = lowXRange
        self.highXRange = highXRange
        self.convert_exp_data = convert_exp_data
        if exp_data:
            self.exp_data = exp_data
            self.__processExpData()
        self.__getData()
        self.plot_exp_data = plot_exp_data
        self.plot_maxCS_data = plot_maxCS_data
        self.show_bass_barrier = show_bass_barrier
        self.reaction_info_note = reaction_info_note
        self.save_note = save_note

        if len(channels_to_plot) == 0:
            self.channels_to_plot = self.data_ifus0["isotope"].unique()
        else:
            # add to self.channels_to_plot only those that are in the data
            self.channels_to_plot = []
            for channel in channels_to_plot:
                if np.any(self.data_ifus0["isotope"].unique() == channel):
                    self.channels_to_plot.append(channel)

        if lowYRange == 0:
            self.lowYRange = self.__lowYRange()

        if highYRange == 0:
            self.highYRange = self.__highYRange()

        if lowXRange == 0:
            self.lowXRange = self.__lowXRange()

        if highXRange == 0:
            self.highXRange = self.__highXRange()

        if self.bf_diff > 0:
            self.__getBfDiffData()

    def isotopeA(self, isotope):
        return int(splitIsotope(isotope)[0])

    def isotopeElement(self, isotope):
        return splitIsotope(isotope)[1]

    def isotopeZ(self, isotope):
        for element in periodicTable["elements"]:
            if element["symbol"] == self.isotopeElement(isotope):
                return element["number"]
        return None

    def getAllIsotopes(self):
        # first check if IFUS0 and IFUS10 have the same isotopes, then return all of them in a list
        if (
            self.data_ifus0["isotope"].unique() == self.data_ifus10["isotope"].unique()
        ).all():
            return self.data_ifus0["isotope"].unique()
        else:
            raise ValueError("IFUS0 and IFUS10 do not contain the same isotopes")

    def __loadMasses(self):
        mass_dict = getMassTable()

        try:
            self.m_proj = mass_dict[self.projectile]
            self.m_targ = mass_dict[self.target]
            self.m_cn = mass_dict[self.cn]
        except KeyError as e:
           raise ValueError(f"Mass for isotope {e} not found in masses.dat")

    def __getData(self):
        # get data into variable
        try:
            self.data_ifus0 = pd.read_csv(
                PATH_TO_HIVAPS
                + "/"
                + self.cn.lower()
                + "/data/"
                + self.projectile
                + "_"
                + self.target
                + "_"
                + self.cn
                + "_"
                + self.evap_channel
                + "_"
                + "IFUS0"
                + "_BF"
                + f"{self.barfac:.2f}"
                + "_sigr"
                + str(self.sigr)
                + "_V0"
                + str(self.V0)
                + "_R"
                + str(self.R0)
                + ".dat",
                sep="\t",
            )

            self.data_ifus10 = pd.read_csv(
                PATH_TO_HIVAPS
                + "/"
                + self.cn.lower()
                + "/data/"
                + self.projectile
                + "_"
                + self.target
                + "_"
                + self.cn
                + "_"
                + self.evap_channel
                + "_"
                + "IFUS10"
                + "_BF"
                + f"{self.barfac:.2f}"
                + "_sigr"
                + str(self.sigr)
                + "_V0"
                + str(self.V0)
                + "_R"
                + str(self.R0)
                + ".dat",
                sep="\t",
            )

            self.data_ifus0 = self.data_ifus0.melt(
                id_vars=["E_lab", "E*/MeV"], var_name="isotope", value_name="CS"
            )
            self.data_ifus10 = self.data_ifus10.melt(
                id_vars=["E_lab", "E*/MeV"], var_name="isotope", value_name="CS"
            )

            self.__scaleData(self.data_ifus0)
            self.__scaleData(self.data_ifus10)

        except:
            print(
                f"No data found for the reaction {self.projectile} + {self.target} -> {self.cn}*"
            )
            self.data_ifus0, self.data_ifus10 = None, None

    def __getBfDiffData(self):
        # get data into variable
        try:
            self.data_ifus0_bf_low = pd.read_csv(
                PATH_TO_HIVAPS
                + "/"
                + self.cn.lower()
                + "/data/"
                + self.projectile
                + "_"
                + self.target
                + "_"
                + self.cn
                + "_"
                + self.evap_channel
                + "_"
                + "IFUS0"
                + "_BF"
                + f"{self.barfac-self.bf_diff:.2f}"
                + "_sigr"
                + str(self.sigr)
                + "_V0"
                + str(self.V0)
                + "_R"
                + str(self.R0)
                + ".dat",
                sep="\t",
            )

            self.data_ifus0_bf_high = pd.read_csv(
                PATH_TO_HIVAPS
                + "/"
                + self.cn.lower()
                + "/data/"
                + self.projectile
                + "_"
                + self.target
                + "_"
                + self.cn
                + "_"
                + self.evap_channel
                + "_"
                + "IFUS0"
                + "_BF"
                + f"{self.barfac+self.bf_diff:.2f}"
                + "_sigr"
                + str(self.sigr)
                + "_V0"
                + str(self.V0)
                + "_R"
                + str(self.R0)
                + ".dat",
                sep="\t",
            )

            self.data_ifus10_bf_low = pd.read_csv(
                PATH_TO_HIVAPS
                + "/"
                + self.cn.lower()
                + "/data/"
                + self.projectile
                + "_"
                + self.target
                + "_"
                + self.cn
                + "_"
                + self.evap_channel
                + "_"
                + "IFUS10"
                + "_BF"
                + f"{self.barfac-self.bf_diff:.2f}"
                + "_sigr"
                + str(self.sigr)
                + "_V0"
                + str(self.V0)
                + "_R"
                + str(self.R0)
                + ".dat",
                sep="\t",
            )

            self.data_ifus10_bf_high = pd.read_csv(
                PATH_TO_HIVAPS
                + "/"
                + self.cn.lower()
                + "/data/"
                + self.projectile
                + "_"
                + self.target
                + "_"
                + self.cn
                + "_"
                + self.evap_channel
                + "_"
                + "IFUS10"
                + "_BF"
                + f"{self.barfac+self.bf_diff:.2f}"
                + "_sigr"
                + str(self.sigr)
                + "_V0"
                + str(self.V0)
                + "_R"
                + str(self.R0)
                + ".dat",
                sep="\t",
            )

            self.data_ifus0_bf_low = self.data_ifus0_bf_low.melt(
                id_vars=["E_lab", "E*/MeV"], var_name="isotope", value_name="CS"
            )
            self.data_ifus0_bf_high = self.data_ifus0_bf_high.melt(
                id_vars=["E_lab", "E*/MeV"], var_name="isotope", value_name="CS"
            )

            self.data_ifus10_bf_low = self.data_ifus10_bf_low.melt(
                id_vars=["E_lab", "E*/MeV"], var_name="isotope", value_name="CS"
            )
            self.data_ifus10_bf_high = self.data_ifus10_bf_high.melt(
                id_vars=["E_lab", "E*/MeV"], var_name="isotope", value_name="CS"
            )

            self.__scaleData(self.data_ifus0_bf_low)
            self.__scaleData(self.data_ifus0_bf_high)
            self.__scaleData(self.data_ifus10_bf_low)
            self.__scaleData(self.data_ifus10_bf_high)

        except:
            print(
                f"No data found for difference plotting for reaction {self.projectile} + {self.target} -> {self.cn}*"
            )
            (
                self.data_ifus0_bf_low,
                self.data_ifus0_bf_high,
                self.data_ifus10_bf_low,
                self.data_ifus10_bf_high,
            ) = (None, None, None, None)

    def __scaleData(self, dataframe):
        scale = 1
        if self.unit == "mb":
            scale = 1
        elif self.unit == "ub":
            scale = 1e3
        elif self.unit == "nb":
            scale = 1e6
        elif self.unit == "pb":
            scale = 1e9

        dataframe["CS"] = dataframe["CS"].multiply(scale)

    def getEnergyColumn(self):
        if self.energy_values == "beam":
            return "E_lab"
        elif self.energy_values == "exc":
            return "E*/MeV"
        else:
            raise ValueError("energy_values must be 'beam' or 'exc'")

    def getMinEnergy(self, energy_mode="beam"):
        if energy_mode == "beam":
            if self.E_lab is None:
                raise ValueError("E_lab not provided")
            return min(self.E_lab)

        elif energy_mode == "exc":
            if self.E_exc is None:
                raise ValueError("E_exc not provided")
            return min(self.E_exc)

        else:
            raise ValueError("energy_mode must be 'beam' or 'exc'")

    def getMaxEnergy(self, energy_mode="beam"):
        if energy_mode == "beam":
            if self.E_lab is None:
                raise ValueError("E_lab not provided")
            return max(self.E_lab)

        elif energy_mode == "exc":
            if self.E_exc is None:
                raise ValueError("E_exc not provided")
            return max(self.E_exc)

        else:
            raise ValueError("energy_mode must be 'beam' or 'exc'")


    def __lowYRange(self):
        # find maximum of the 'smallest' excit. function (IFUS10) to be plotted and then set the minimum to 1 order lower, or min of exp data if it is lower
        lowest_max = float("inf")
        for channel in self.channels_to_plot:
            if (
                self.data_ifus10[self.data_ifus10["isotope"] == channel]["CS"].max() > 0
                and self.data_ifus10[self.data_ifus10["isotope"] == channel]["CS"].max()
                < lowest_max
            ):
                lowest_max = self.data_ifus10[self.data_ifus10["isotope"] == channel][
                    "CS"
                ].max()

        try:
            return self.roundMinYRange(
                self.exp_data.getMinCS()
                if self.exp_data.getMinCS() < lowest_max
                else lowest_max
            )
        except:
            return self.roundMinYRange(lowest_max)

    def __highYRange(self):
        # find maximum of the 'largest' excit. function (IFUS10) to be plotted and set the maximum to 1 order higher, or max of exp data if it is higher
        highest_max = 0
        for channel in self.channels_to_plot:
            if (
                self.data_ifus10[self.data_ifus10["isotope"] == channel]["CS"].max() > 0
                and self.data_ifus10[self.data_ifus10["isotope"] == channel]["CS"].max()
                > highest_max
            ):
                highest_max = self.data_ifus10[self.data_ifus10["isotope"] == channel][
                    "CS"
                ].max()

        try:
            return self.roundMaxYRange(
                self.exp_data.getMaxCS()
                if self.exp_data.getMaxCS() > highest_max
                else highest_max
            )
        except:
            return self.roundMaxYRange(highest_max)

    def roundMinYRange(self, value):
        return 10 ** round(log10(value)) / 10

    def roundMaxYRange(self, value):
        return 10 ** round(log10(value)) * 10

    def __lowXRange(self):
        # get minimum energy for which the CS value is larger than lowYRange or minimum of  E_lab of exp data if it is lower
        try:
            return min(
                self.roundMinXRange(
                    self.data_ifus10[
                        self.data_ifus10["isotope"].isin(self.channels_to_plot)
                    ][self.data_ifus10["CS"] > self.lowYRange][self.getEnergyColumn()].min()
                ),
                self.exp_data.getMinEnergy(self.energy_values) - 5
            )
        except:
            return self.roundMinXRange(
                self.data_ifus10[
                    self.data_ifus10["isotope"].isin(self.channels_to_plot)
                ][self.data_ifus10["CS"] > self.lowYRange][self.getEnergyColumn()].min()
            )

    def __highXRange(self):
        # get maximum energy for which the CS value is larger than lowYRange or minimum of  E_lab of exp data if it is lower
        try:
            return max(
                self.roundMaxXRange(
                    self.data_ifus10[
                        self.data_ifus10["isotope"].isin(self.channels_to_plot)
                    ][self.data_ifus10["CS"] > self.lowYRange][self.getEnergyColumn()].max()
                ),
               self.exp_data.getMaxEnergy(self.energy_values) + 5
            )
        except:
            return self.roundMaxXRange(
                self.data_ifus10[
                    self.data_ifus10["isotope"].isin(self.channels_to_plot)
                ][self.data_ifus10["CS"] > self.lowYRange][self.getEnergyColumn()].max()
            )

    def roundMinXRange(self, value):
        return floor(value / 10) * 10

    def roundMaxXRange(self, value):
        return ceil(value / 10) * 10

    def getBassBarrier(self):
        if self.energy_values == "beam":
            return self.getBassBarrierLab()

        elif self.energy_values == "exc":
            return self.getBassBarrierExc()

        else:
            raise ValueError("energy_values must be 'beam' or 'exc'")

    def getBassBarrierLab(self):
        A_p = self.isotopeA(self.projectile)
        Z_p = self.isotopeZ(self.projectile)

        A_t = self.isotopeA(self.target)
        Z_t = self.isotopeZ(self.target)

        R_12 = 1.07 * (A_p ** (1 / 3) + A_t ** (1 / 3))

        Bass_cm = Z_p * Z_t * 1.44 / (R_12 + 2.7) - 2.9 * (
            A_p ** (1 / 3) * A_t ** (1 / 3) / (A_p ** (1 / 3) + A_t ** (1 / 3))
        )

        return Bass_cm * (A_p + A_t) / A_t

    def getBassBarrierExc(self):
        if not hasattr(self, "m_proj"):
            self.__loadMasses()

        B_lab = self.getBassBarrierLab()

        A_p = self.isotopeA(self.projectile)
        A_t = self.isotopeA(self.target)

        E_cm = B_lab * A_t / (A_p + A_t)

        Q = (self.m_proj + self.m_targ - self.m_cn) * 931.494

        return E_cm + Q

    def plot(
        self,
        plot_diff=True,
        plot_exp_data=True,
        alpha_value=0.15,
        show_reaction_info=True,
        reaction_info_note="",
        show_bass_barrier=True,
        display_plot=True,
    ):
        if not show_bass_barrier:
            show_bass_barrier = self.show_bass_barrier
        if self.reaction_info_note:
            reaction_info_note = self.reaction_info_note
        fig, ax = plt.subplots(figsize=(12, 5.5))

        sns.lineplot(
            x=self.getEnergyColumn(),
            y="CS",
            hue="isotope",
            hue_order=self.channels_to_plot,
            data=self.data_ifus10[
                self.data_ifus10["isotope"].isin(self.channels_to_plot)
            ],
            #palette=colors,
            palette=colors[:len(self.channels_to_plot)],
        )
        sns.lineplot(
            x=self.getEnergyColumn(),
            y="CS",
            hue="isotope",
            hue_order=self.channels_to_plot,
            data=self.data_ifus0[
                self.data_ifus0["isotope"].isin(self.channels_to_plot)
            ],
            legend=None,
            linestyle="--",
            #palette=colors,
            palette=colors[:len(self.channels_to_plot)],
        )
        for text in plt.legend(
            loc="upper right",
            framealpha=1,
            title=r"$^{"
            + str(self.isotopeA(self.cn))
            + "}$"
            + self.isotopeElement(self.cn)
            + r"$^*$",
            title_fontsize=18,
            fontsize=16,
        ).get_texts():
            label = text.get_text()
            text.set_text(
                "$^{" + str(self.isotopeA(label)) + "}$" + self.isotopeElement(label)
            )

        plt.semilogy()
        plt.ylim(self.lowYRange, self.highYRange)
        plt.xlim(self.lowXRange, self.highXRange)
        if self.unit == "ub":
            plt.ylabel(r"$\sigma$ [$\mu$b]", fontsize=20)
        else:
            plt.ylabel(rf"$\sigma$ [{self.unit}]", fontsize=20)

        #plt.xlabel("$E_{proj}$ [MeV]", fontsize=20)
        if self.energy_values == "beam":
            plt.xlabel(r"$E_{beam}$ [MeV]")
        else:
            plt.xlabel(r"$E^*$ [MeV]")

        if show_reaction_info:
            plt.text(
                0.01,
                0.99,
                r"$^{"
                + str(self.isotopeA(self.projectile))
                + "}$"
                + self.isotopeElement(self.projectile)
                + r" + $^{"
                + str(self.isotopeA(self.target))
                + "}$"
                + self.isotopeElement(self.target)
                + r" $\rightarrow$ $^{"
                + str(self.isotopeA(self.cn))
                + "}$"
                + self.isotopeElement(self.cn)
                + r"$^*$, BF = "
                + str(self.barfac)
                + str("" if self.bf_diff == 0 else (r" $\pm$ " + str(self.bf_diff))),
                ha="left",
                va="top",
                transform=ax.transAxes,
            )

            if reaction_info_note:
                plt.title(reaction_info_note, fontsize=12)

        if plot_diff and self.plot_diff and self.bf_diff > 0:
            self.__plotBfDiff(alpha_value)

        if plot_exp_data and self.plot_exp_data:
            self.__plotExpData()

        if show_bass_barrier or self.show_bass_barrier:
            try:
                barrier = self.getBassBarrier()
            except Exception as e:
                print("Bass barrier not plotted:", e)
                return            
            
            if barrier > (self.lowXRange + 5 / 100 * (self.highXRange - self.lowXRange)):
                plt.annotate(
                    r"$B_{Bass}$",
                    xy=(barrier, self.lowYRange),
                    xytext=(
                        barrier,
                        10 ** (log10(self.lowYRange) + 0.15 * (log10(self.highYRange) - log10(self.lowYRange))
                        ),
                    ),
                    ha="center",
                    fontsize=20,
                    arrowprops=dict(arrowstyle="->", color="black", linewidth=2),
                )   

        if display_plot:
            plt.show()
        return self

    def __plotBfDiff(self, alpha_value):
        try:
            for index, channel in enumerate(self.channels_to_plot):
                plt.fill_between(
                    self.data_ifus0[self.data_ifus0["isotope"] == channel]["E_lab"],
                    self.data_ifus0[self.data_ifus0["isotope"] == channel]["CS"],
                    self.data_ifus0_bf_low[
                        self.data_ifus0_bf_low["isotope"] == channel
                    ]["CS"],
                    color=colors[index],
                    alpha=alpha_value,
                )

                plt.fill_between(
                    self.data_ifus0[self.data_ifus0["isotope"] == channel]["E_lab"],
                    self.data_ifus0[self.data_ifus0["isotope"] == channel]["CS"],
                    self.data_ifus0_bf_high[
                        self.data_ifus0_bf_high["isotope"] == channel
                    ]["CS"],
                    color=colors[index],
                    alpha=alpha_value,
                )

                plt.fill_between(
                    self.data_ifus10[self.data_ifus10["isotope"] == channel]["E_lab"],
                    self.data_ifus10[self.data_ifus10["isotope"] == channel]["CS"],
                    self.data_ifus10_bf_low[
                        self.data_ifus10_bf_low["isotope"] == channel
                    ]["CS"],
                    color=colors[index],
                    alpha=alpha_value,
                )

                plt.fill_between(
                    self.data_ifus10[self.data_ifus10["isotope"] == channel]["E_lab"],
                    self.data_ifus10[self.data_ifus10["isotope"] == channel]["CS"],
                    self.data_ifus10_bf_high[
                        self.data_ifus10_bf_high["isotope"] == channel
                    ]["CS"],
                    color=colors[index],
                    alpha=alpha_value,
                )
        except:
            pass

    def __processExpData(self):
        self.__checkIsotopesInData()
        if self.convert_exp_data:
            self.exp_data.scaleExpData(self.unit)

    def __checkIsotopesInData(self):
        exp_data_isotopes = set(self.exp_data.cs_data.keys())
        isotopes_to_show = set(self.channels_to_plot)

        if not exp_data_isotopes.issubset(isotopes_to_show):
            raise ValueError(
                "Experimental data contain isotopes which are not in the selected HIVAPs"
            )

    def __plotExpData(self):
        try:
            for isotope in self.exp_data.getExpEvapResidues():
                if self.plot_maxCS_data:
                    plt.axline(
                        (self.lowXRange, self.exp_data.getMaxChannelCS(isotope)),
                        (self.highXRange, self.exp_data.getMaxChannelCS(isotope)),
                        color=colors[self.channels_to_plot.index(isotope)],
                        ls=":",
                        linewidth=3,
                    )
                else:
                    for exp_data in self.exp_data.getEvapChannelExpData(isotope, energy_mode=self.energy_values):
                        (_, caps, _) = plt.errorbar(
                            exp_data[0],
                            exp_data[1],
                            yerr=[[exp_data[2]], [exp_data[3]]],
                            marker=markers[self.channels_to_plot.index(isotope)],
                            color=colors[self.channels_to_plot.index(isotope)],
                            ls="none",
                            markersize=7,
                            capsize=5,
                        )
                        for cap in caps:
                            cap.set_markeredgewidth(1)
        except:
            print(
                f"No exp data entered for reaction {self.projectile} + {self.target} -> {self.cn}*"
            )

    def saveFig(self, save_note="", extension="pdf"):
        if self.save_note:
            save_note = self.save_note

        extension_types = ["pdf", "svg", "png"]
        if extension not in extension_types:
            raise ValueError(
                "Invalid extension type, please choose one from: %s" % extension_types
            )
        
        if not os.path.exists('./figs'):
            os.makedirs('./figs')

        plt.savefig(
            "figs/"
            + self.projectile
            + "_"
            + self.target
            + "_"
            + self.cn
            + "_"
            + self.evap_channel
            + "_barfac"
            + f"{self.barfac:.2f}"
            + "_sigr"
            + str(self.sigr)
            + str("" if len(save_note) == 0 else "_")
            + save_note
            + "."
            + extension,
            bbox_inches="tight",
        )
