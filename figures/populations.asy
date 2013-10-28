import node;
import roundedpath;

defaultnodestyle = nodestyle (xmargin = 2pt, textpen = Helvetica ("m", "n"));
defaultdrawstyle = drawstyle(arrow = Arrow (6));

node s0 = scircle ("0");
node s1 = scircle ("1");
node s2 = scircle ("2");
node s3 = scircle ("3");

node t0 = scircle ("0");
node t1 = scircle ("1");
node t2 = scircle ("2");
node t3 = scircle ("3");
node t4 = scircle ("4");

real h = 3cm;
real v = 1cm;

s0 << edown (v) << s1 << edown (v) << s2 << edown (v) << s3 << eup (3.5*v);
s0 << eright (h) << t0;
t0 << eup (v/2) << t0;
t0 << edown (v) << t1 << edown (v) << t2 << edown (v) << t3 << edown (v) << t4;

draw (s0, s1, s2, s3, t0, t1, t2, t3, t4);

draw (s0--t1,
      s1--t1,
      s1--t2,
      s3--t3,
      s2--t3,
      s0--t4);

pair d = (0.6cm, -0.6cm);

draw (roundedpath (box (s0.pos - d, s3.pos + d - (0, 0.4cm)), 3), L="$P_s$");
draw (roundedpath (box (t0.pos - d, t4.pos + d - (0, 0.4cm)), 3), L="$P_t$");
