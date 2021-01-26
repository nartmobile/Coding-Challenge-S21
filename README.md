# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Libraries Used
1. [DNA Features Viewer](https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer)

## Sources Used
1. [DNA Features Viewer Documentation](https://edinburgh-genome-foundry.github.io/DnaFeaturesViewer/)
2. [DNA Features Viewer Research Paper](https://www.biorxiv.org/content/10.1101/2020.01.09.900589v1.full.pdf)

## Process
The first step I took to solve this problem was find out what a circular genome map was to begin with. I started by looking up "circle dna map" on Google. The results I got were various YouTube videos and Google Image results that looked like an absolute mess of charts and colors. I tried to understand what exactly I was looking at by looking through the videos but they weren't very helpful. What ended up helping me understand the data I was working with was by looking up .gb files and finding a trail to the NCBI. On there was a database of tons of GenBank records that I learned detailed gene information.

The next step I took was finding out how to create the graphical representations of these files. I remembered that the README had hinted at using Python as it was the simplest, and sure enough, the first library that came up was the DNA Features Viewer in Python. The documentation provided examples for both standard "line" charts and circular charts. I messed around with the default classes that were used to render each graph and found where the data was entered. The problem I encountered, however, was importing data from a GenBank file itself. The documentation also provided a class that imported GenBank data and sample code that rendered the data to a line graph. I struggled to find a way to make it render in a circle.

I continued looking online in hopes of finding an example of someone who was able to render .gb data into a circle using this library. I knew it was possible because the website hosted by the makers of the library allowed users to upload sample data and graph it without downloading the library itself and running code. I eventually found a research paper written by whom I presume to be the makers of the library. Within their samples of data, they included a code snippet that showed the parameter that changed the "render module" from GraphicRecord to CircularGraphicRecord. From there, I was able to modify my own class and output the graph that I have submitted.
