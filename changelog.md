https://github.com/UBC-MDS/data-analysis-review-2023/issues/15

Below is a summary of the feedback we've recieved to improve our project.

Feedback:
1. You have the LICENSE.md file but do not have the Creative Commons license in the file. (I also do not have this in my group, and it was not made clear on how to do this but I think it is just adding some more things to your LICENSE.md file).

2. Link reference.bib to the notebook: Associating the reference.bib file with the notebook will improve documentation and citation practices.

3. Create an HTML file of the project: Generating an HTML file will facilitate easy sharing and viewing of the project.

4. Host the 'build' folder (Jupyter Book): Utilizing the build folder by hosting it would make the project more accessible and navigable. The figure labels not rendering correctly because of this.

5. Consider resorting the plots: Reordering the plots can enhance readability and comprehension, offering a more structured visualization.

6. I found the explanation for the tests to be vague in both the readme and the actual test scripts.

7. The file names were inconsistent. In the src folder we see some files being named helper_, and test_ or tests_ and others having a different name convention.

8. For the histograms it might be better to unstack the histograms as we are comparing values between the two groups and not the sum of the values

9. The figure to show the coefficients of the model would be clearer if you sorted the coefficients in either ascending or descending order

10. The container did not work when I tried to build it.
The repo is lacking the docker-compose.yml file (all 4 reviewers noted this feedback)

Response to feedback & further improvements to our project:

2. We linked the contents in our references.bib with the relveant sections of our report and our bibliography. This can be viewed at
   UBC-MDS.github.io/2023-dsci522-group22/.
   Navigate to https://github.com/UBC-MDS/2023-DSCI522-Group22/blob/main/report/references.bib to view the modified reference entries.
4. In milestone 3, our report was not rendering properly on our github.com pages. We agree that was a key component of this project, so we added them at
   UBC-MDS.github.io/2023-dsci522-group22/. You will now notice there is a /docs folder and the HTML files were moved to that location to be rendered.
5. We decided that the current order of the plots were sufficient for readability and comprehension. We respectivefully disagreed with this advice. It was general 
   and didn't offer a suggestion how our plots should be ordered.
8. This advice was not applicable, as our histograms weren't stacked additively, they were side by side. We think the visualization choice is sufficient to display 
    our thesis.

Changes from Chun Li
1. Updated LICENSE file based on the feedback received from Peer Review
2. Updated the environment.yaml file to include the Make version 4.4.1
3. Updated the Dockerfile to include Make version 4.4.1
4. Rebuilt the Docker image and pushed it to Docker Hub remote repo
