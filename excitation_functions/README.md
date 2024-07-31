# Excitation function plotting script
## Script for plotting the excitation functions from HIVAP and corresponding experimental data

To plot the excitation functions, run file plot_excitation_functions.py with python (you may have to install required packages - numpy, pandas, etc.):
~~~
python3 plot_excitation_functions.py
~~~

### Create a reaction object in reactions_list.py file (or append to existing array of Reactions):
~~~
Reaction(
        projectile,
        target,
        cn,
        barfac,
        sigr,
        unit="mb",
        evap_channel="xn",
        bf_diff=0.00,
        plot_diff=True,
        channels_to_plot=None,
        lowYRange=0,
        highYRange=0,
        lowXRange=0,
        highXRange=0,
        exp_data: ExpData = None,
        plot_exp_data=True,
        plot_maxCS_data=False,
        show_bass_barrier=False,
        reaction_info_note="",
        save_note=""
)
~~~

unit - change units in which data are plotted: 'mb' (default), 'ub' or 'nb'

evap_channel - change which evap. channels are displayed: 'xn' (default), 'pxn' or '2pxn'

bf_diff - specify a BARFAC "uncertainty", which will be displayed as a shaded area around the main value: 0.0 (default)

plot_diff - turn off the BARFAC difference plotting: default True

channels_to_plot - specify which channels are to be plotted

low[axis]Range/high[axis]Range - change the range of [axis] manually

exp_data - explained in detail below

plot_exp_data - specify if to plot experimental data: default True

plot_maxCS_data - if only max CS values are available without specified beam energy, a horizontal line is plotted: default False

show_bass_barrier - plots an arrow at the Bass barrier lab frame energy: default False

reaction_info_note - adds title with custom note to the plot, if not empty

save_note - appends note to the end of the resulting plot file name, if not empty

### Experimental data

Experimental data are entered in the following form:

~~~
ExpData(
    E_lab = [laboratory energies],
    cs_data = {
        'Isotope': 
        [
            Cross section values
        ]
    },
    error_data = {
        'Isotope':
        [
            [low assymetric error or symmetric error],
            [high assymetric error; if symmetric error is used, don't fill this array]
        ]
    }
)
~~~

E_lab - energies in the laboratory frame

Isotope - must be also included in the Reaction's "channels_to_plot" or in HIVAP data

Cross section values - array of cross sections in milibarns(!) corresponding to the E_lab - must be of the same size

error_data - optional, in milibarns(!);

'Isotope' in error_data must be also in cs_data

Both arrays (or the first one if symmetric errors are used) for each isotope in error_data must have the same size as E_lab

---

#### Assymetric error example:
~~~
ExpData(E_lab=[230, 240], {'193At': [0.15, 15]}, error_data={'193At': [[0.1, 10], [0.2, 20]]})
~~~
Two data points:
- at 230 MeV - 0.15 mb with (-0.1 +0.2) assymetric errors
- at 240 MeV - 15 mb with (-10 + 20) assymetric errors

---

#### Symmetric error example:
~~~
ExpData(E_lab=[230, 240], {'193At': [0.15, 15]}, error_data={'193At': [[0.1, 10]]})
~~~

Two data points:
- at 230 MeV - 0.15 mb +- 0.1 mb
- at 240 MeV - 15 mb +- 10 mb
