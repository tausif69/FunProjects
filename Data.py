#bokeh graph

from bokeh.plotting import figure
from bokeh.io import output_file, show
#data
x = [1,2,3,4,5]
y = [6, 7, 8, 9, 10]

#prepareOutput

output_file("Line.html")
f = figure()
f.line(x,y)

show(f)




#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x1=[3,7.5,10]
y1=[3,6,9]

#prepare the output file
output_file("Line2.html")

#create a figure object
f2=figure()

#create line plot
f2.triangle(x1,y1)

#write the plot in the figure object
show(f2)
#Snippet producing the circle based plot

#Making a basic Bokeh line graph

#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

#prepare some data
x2=[3,7.5,10]
y2=[3,6,9]

#prepare the output file
output_file("Line3.html")

#create a figure object
f3=figure()

#create line plot
f3.circle(x2,y2)

#write the plot in the figure object
show(f3)
