set term png

set xl "x" # tytuł osi x
set yl "y" # tytuł osi y
set style line 1 \
    linecolor rgb '#FF0000' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5

set out "startPath.png"
plot 'startPath.dat' with linespoints linestyle 1;

set out "finalPath.png"
plot 'finalPath.dat' with linespoints linestyle 1