//usepackage("amsfonts");
int n = 5;

real y0 = 0.375;
real x1 = 0.5;
real bs = 0.05;
real alen = (5 + 1) * bs;

size(200 * (1.0 + x1),200);
//filldraw(box((0,0),(0.5,0.5)),lightgray,black);
draw((0,y0)..(0,y0 + alen), black, Arrow);
draw((0,y0)..(alen,y0), black, Arrow);
//label("$\mathbb{N}_X$", (0.25,-0.05));
//label("$\mathbb{N}_Y$", (-0.06,0.25));
real d = 0.02;
//draw((0.35,0.63-d)..(0.35,0.4+d));
//draw((0.36+d,0.65)..(0.6-d,0.65));

pair[] m = {(0,1), (1,1), (1,2), (3,2), (2,3), (0,4)};

for (pair p : m)
  {
    real i=p.x;
    real j=p.y;
    fill(box((bs * i,y0 + bs * j),(bs * (i + 1), y0 + bs * (j + 1))), gray);
  }

for (int i = 0; i < n; ++i)
  {
    draw((0,y0 + bs * (i + 1))..(bs * n, y0 + bs * (i + 1)), p=dotted);
    draw((bs * (i + 1), y0)..(bs * (i + 1), y0 + bs * n), p=dotted);
  }
