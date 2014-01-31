//usepackage("amsfonts");
int n = 9;

real bs = 0.05;
real y0 = 0.375 + n * bs;
real x1 = 0.5;
real alen = (9 + 1) * bs;

real dtxt = 0.01 * (n + 1) / (5 + 0.5);

size(280 * (1.0 + x1),280);
//filldraw(box((0,0),(0.5,0.5)),lightgray,black);
draw((0,y0)..(0,y0 - alen), black, Arrow);
draw((0,y0)..(alen,y0), black, Arrow);
label("sources", p=fontsize(14pt), (0.5 * alen, y0 + dtxt));
label(rotate(90)*"targets", p=fontsize(14pt), (- dtxt, y0 - 0.5 * alen));
//label("$\mathbb{N}_X$", (0.25,-0.05));
//label("$\mathbb{N}_Y$", (-0.06,0.25));
real d = 0.02;
//draw((0.35,0.63-d)..(0.35,0.4+d));
//draw((0.36+d,0.65)..(0.6-d,0.65));

for (int i = 0; i < n; ++i)
  {
    int j=i;
    fill(box((bs * i,y0 - bs * j),(bs * (i + 1), y0 - bs * (j + 1))), gray);
  }

for (int i = 0; i < n; ++i)
  {
    draw((0,y0 - bs * (i + 1))..(bs * n, y0 - bs * (i + 1)), p=dotted);
    draw((bs * (i + 1), y0)..(bs * (i + 1), y0 - bs * n), p=dotted);
  }

// Better way to make ellipses?
for (int i = 0; i < 3; ++i)
  {
    fill(circle((n*bs+0.01*(i + 1),y0 - n*bs-0.01* (i + 1)),0.0025));
  }

draw(box((0,y0), (bs * 7, y0 - bs * 7)));
