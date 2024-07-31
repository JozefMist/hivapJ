import time

from util import loadReactions

if __name__ == "__main__":
    reactions = loadReactions()

    start = time.time()
    for i, reaction in enumerate(reactions):
        print('Running', i+1, '/', len(reactions))
        reaction.plot(show_reaction_info=True, show_bass_barrier=True, display_plot=False)
        reaction.saveFig()
        
    end = time.time()

    print('Execution time:', end-start, 's')