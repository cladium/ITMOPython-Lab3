# LiS keygen (not real ofc)

Since tkinter does not support external fonts, you will have to convert .ttf into a set of separate .png files with a transparent background for each character. To do this, use FontForge (.ttf -> .svg) and then cairo (.svg -> .png). Since Windows is the best operating system in the world, it does not have the cairo library by default, nor is there an easy and convenient way to install it. Therefore, the cairosvg module for Python will not work out of the box. 

To convert .ttf -> .svg, you need to add the path to the FontForge binaries to the PATH, and then run the command:

```ffpython export.py```

After that, you can run ```convert.py``` which converts .svg from the ```svg_export``` folder to .png to the ```png``` folder. The size of the symbol can be changed.