from fontforge import *
font = open("Dudu_Calligraphy.ttf")

# export minus
glyph = nameFromUnicode(45)
font[glyph].export("svg_export/" + font[glyph].glyphname + ".svg")

# export numbers
for position in range(48, 58):
    glyph = nameFromUnicode(position)
    font[glyph].export("svg_export/" + font[glyph].glyphname + ".svg")
    
# export letters
for position in range(65, 91):
    glyph = nameFromUnicode(position)
    font[glyph].export("svg_export/" + font[glyph].glyphname + ".svg")
