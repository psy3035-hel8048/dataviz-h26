# Workshop 2 - Imports, the terminal, and reading in data

In the second workshop, we will introduce you to installing and importing libraries and packages. In doing this we will use the command prompt (terminal). After this, we will load in some data and beging plotting it.

The data we will use is here: [Pearson.txt](../data/Pearson.txt)

Some useful videos related to the workshop material are pasted in [Additional info](workshop2.md#additional-info) and the powerpoint can be found [here](../powerpoints/PSY3035-HEL8048_Lecture%202_Imports,%20CLI,%20and%20Data.pptx).


## Post-workshop summary
There was a lot of troubleshooting of VS Code and associated issues to do with your Python environments and installations. I think everybody had things working at the end. See links at the end of the document.  

## Tidying up from Workshop 2
By the end of the session, most people had been able to load in the Pearson.txt data file. Some had even made a figure with it. Everybody should try to go through the slides in the presentation that we didn't quite get to (the ones that involve subsetting the data (e.g. `fathers = data[:,0]`) and making a figure (e.g. `f, ax = plt.subplots()`)).

If you are stuck on this, then please reach out to me by email or on Github/Canvas. I will try to arrange a time when we can meet up and get things working.

## Preparation for Workshop 3
We will start talking about data visualisation in our next workshop. In preparation, I would like everybody to bring a figure (i.e., a graph or some way data has been visualised) and you should be able to say one thing you like about it or one thing you don't. For example, good things are that it might show the data in a creative or intuitive way, it might have a nice colour palette. Bad things might be that it is impossible to understand, it misrepresents the data, or it just looks terrible. You could find the figure anywhere including in a paper you're reading for your research project, in a newspaper stury, or even from a poster in the corridor.

## Extra hour for next week
I have a meeting next Monday, which means I will need to leave at 16:00. I don't want to deprive you of the extra hour so I have set up a poll that can help us find another time for this hour.

https://beta.framadate.org/polls/9aaa4db9555f4c701e47

If you don't think you need or want the extra hour, that's fine, you can just ignore the poll.

## Additional info

### Simple explanation of the terminal:
[video](https://www.youtube.com/watch?v=qN9lNgs6wJ0)

### A bit of a deeper dive on the terminal
[video](https://www.youtube.com/watch?v=mABpAI-pCw0)

(first 8 min good explanation, then it gets into the hands-on bit which you will have to open your own terminal etc rather than a "scrimba terminal")

### Unix commands in a Windows terminal
Several of you with Windows machines were unable to run the command `ls` to get the directory contents. This is because it is for the Unix OS, which is used on Macs and Linux computers but not Windows. We can chat more about the differences between these OSs at a later date if people are interested. Until then you have two options:
1. Use `dir` instead of `ls` (it does the same thing)
2. Install the unix commands by running `conda install m2-base` in an Anaconda terminal



