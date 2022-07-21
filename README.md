# tutorials

This is a brief guide to the existing tutorals and which ones may be relevant to your needs. All should read the
introduction to get an outline of what the ASDF format is all about. The introduction does not have any code and
consists only of text. Read the rest in order if you are intent on reading them all. For those that have a narrower
need, see the descriptions for what is covered.

- `High_Level_Introduction_to_ASDF.ipynb`: A pure text outline of what the format is for and why it was developed.
- `Anatomy_of_an_ASDF_file.ipynb`: A basic introduction to the format with examples and exercises. Recommended for the
  less impatient.
- `Reading_a_JWST_ASDF_file.ipynb`: This tutorial uses a file more complex and what is more similar to what JWST data
  will look like. It shows tools to list and search for items within a file. Even if you are not interested in JWST
  data, this aspect is quite useful to understand. One can start with this tutorial if one must deal with JWST ASDF
  files and just can't wait to go through the Anatomy_of_an_ASDF tutorial.
- `ASDF_and_World_Coordinate_Systems.ipynb`: This tutorial is actually more focussed on the Generalized World Coordinate
  System than ASDF (which JWST uses extensively). ASDF is an essential element of GWCS since ASDF is used to save GWCS
  instances and enable its use with data. If your main focus is GWCS, you may try to start with this tutorial, but tools
  from the other tutorials will be useful here.
- `Validation_and_Dealing_with_Errors.ipynb`: This is mostly intended as a reference of how to deal with errors
  encountered with ASDF files. Normally one would read this when having an actual error to figure out what is wrong.
