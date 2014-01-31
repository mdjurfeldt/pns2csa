//usepackage("amsfonts");
int n = 9;

real bs = 0.05;
real y0 = 0.375 + n * bs;
real x1 = 0.5;
real alen = (n + 1) * bs;

real dtxt = 0.01 * (n + 1) / (5 + 0.5);

size(280 * (1.0 + x1),280);
//filldraw(box((0,0),(0.5,0.5)),lightgray,black);
//label("$\mathbb{N}_X$", (0.25,-0.05));
//label("$\mathbb{N}_Y$", (-0.06,0.25));
real d = 0.02;
//draw((0.35,0.63-d)..(0.35,0.4+d));
//draw((0.36+d,0.65)..(0.6-d,0.65));

fill(box((0,y0),(bs * (n + 0.5), y0 - bs * (n + 0.5))), gray);
for (int i = 0; i < (n + 1); ++i)
  {
    for (int j = 0; j < (n + 1); ++j)
      {
	if (i == j || unitrand () < 0.5)
	  fill(box((bs * i,y0 - bs * j),(bs * (i + 1), y0 - bs * (j + 1))), white);
      }
  }

draw((0,y0)..(0,y0 - alen), black, Arrow);
draw((0,y0)..(alen,y0), black, Arrow);
label("sources", p=fontsize(14pt), (0.5 * alen, y0 + dtxt));
label(rotate(90)*"targets", p=fontsize(14pt), (- dtxt, y0 - 0.5 * alen));

for (int i = 0; i < n; ++i)
  {
    draw((0,y0 - bs * (i + 1))..(bs * (n + 0.5), y0 - bs * (i + 1)), p=dotted);
    draw((bs * (i + 1), y0)..(bs * (i + 1), y0 - bs * (n + 0.5)), p=dotted);
  }

// Better way to make ellipses?
for (int i = 0; i < 3; ++i)
  {
    fill(circle((n*bs+0.01*(i + 1),y0 - n*bs-0.01* (i + 1)),0.0025));
  }

//draw(box((0,y0), (bs * 4, y0 + bs * 4)));
//draw(box((0,y0), (bs * 9, y0 + bs * 9)));
