from typing import List, Dict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class ExpData:
    def __init__(
        self,
        E_lab: List[float],
        cs_data: Dict[str, List[float]],
        error_data: Dict[str, List[List[float]]] = {},
    ):
        self.E_lab = E_lab

        self.__checkIsotopesInData(cs_data, error_data)
        self.__checkCSDataLength(cs_data)
        self.__checkErrorDataLength(error_data)
        self.cs_data = cs_data
        self.error_data = error_data

    def __checkCSDataLength(self, data):
        # check that there are CS data for all listed E_lab energies
        for isotope in list(data.keys()):
            if len(self.E_lab) != len(data[isotope]):
                raise ValueError(
                    f"Non-matching length between E_lab and CS data in {isotope}"
                )

    def __checkErrorDataLength(self, data):
        # check that there are error data for all listed E_lab energies and if there are assymetric errors, check their dimension as well
        for isotope in list(data.keys()):
            if data[isotope]:
                if len(self.E_lab) != len(data[isotope][0]):
                    raise ValueError(
                        f"Non-matching length between E_lab and low-error data in {isotope}"
                    )

                if len(data[isotope]) == 2 and len(data[isotope][0]) != len(
                    data[isotope][1]
                ):
                    raise ValueError(
                        f"Non-matching length between high- and low-error data in {isotope}"
                    )

    def __checkIsotopesInData(self, cs_data, error_data):
        # check that isotopes that have errors are also in the CS data
        evap_residues = set(cs_data.keys())
        error_data_isotopes = set(error_data.keys())
        if not error_data_isotopes.issubset(evap_residues):
            raise ValueError("Non-matching isotopes in error data and in CS data")

    def getEvapChannelExpData(self, evap_channel):
        exp_data = []
        if evap_channel not in self.cs_data.keys():
            raise ValueError(
                f"Evaporation channel {evap_channel} is not in the entered exp. data"
            )

        for index, _ in enumerate(self.E_lab):
            if evap_channel not in self.error_data.keys():
                # if not self.error_data[evap_channel]:
                exp_data.append(
                    [
                        self.E_lab[index],
                        self.cs_data[evap_channel][index],
                        np.nan,
                        np.nan,
                    ]
                )
            elif len(self.error_data[evap_channel]) == 1:
                exp_data.append(
                    [
                        self.E_lab[index],
                        self.cs_data[evap_channel][index],
                        self.error_data[evap_channel][0][index],
                        self.error_data[evap_channel][0][index],
                    ]
                )
            elif len(self.error_data[evap_channel]) == 2:
                exp_data.append(
                    [
                        self.E_lab[index],
                        self.cs_data[evap_channel][index],
                        self.error_data[evap_channel][0][index],
                        self.error_data[evap_channel][1][index],
                    ]
                )

        return exp_data

    def getAllExpData(self):
        exp_data = {}

        for isotope in self.cs_data:
            exp_data[isotope] = self.getEvapChannelExpData(isotope)

        return exp_data

    def getMaxChannelCS(self, isotope):
        return max(self.cs_data[isotope])

    def getExpEvapResidues(self):
        return list(self.cs_data.keys())

    def getMinCS(self):
        minimum = float("inf")

        for isotope in self.cs_data.keys():
            if np.nanmin(self.cs_data[isotope]) < minimum:
                minimum = np.nanmin(self.cs_data[isotope])
        return minimum

    def getMaxCS(self):
        maximum = 0

        for isotope in self.cs_data.keys():
            if maximum < np.nanmax(self.cs_data[isotope]):
                maximum = np.nanmax(self.cs_data[isotope])
        return maximum

    def getMaxE_lab(self):
        return max(self.E_lab)

    def getMinE_lab(self):
        return min(self.E_lab)

    def scaleExpData(self, unit):
        if unit not in ["mb", "ub", "nb", "pb"]:
            raise ValueError("Invalid cross section unit")
        scale = 1

        if unit == "mb":
            scale = 1
        elif unit == "ub":
            scale = 1e3
        elif unit == "nb":
            scale = 1e6
        elif unit == "pb":
            scale = 1e9

        for isotope in self.cs_data.keys():
            self.cs_data[isotope] = [scale * i for i in self.cs_data[isotope]]
            try:
                self.error_data[isotope][0] = [
                    scale * i for i in self.error_data[isotope][0]
                ]
                self.error_data[isotope][1] = [
                    scale * i for i in self.error_data[isotope][1]
                ]
            except:
                pass