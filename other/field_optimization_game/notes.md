### Field Opmtimization Game

We have a farmland
- of grid size 9×9
- with F-tiles (farm) & W-tiles (water)
- a farm tile becomes productive if it touches at least one water
	- vertically or horizontally
	- not diagonally
- a productive F contributes 1, regardless of how W it touches

Graph
- each W tile can cover 4 neighbor F tiles
	```
	 F
	FWF
	 F
	```
- W tile touching wastes coverage


Optimize:
- maximize the number of F tiles in the grid that adjacent to at least one W

Theoretical Upper Bounds
- $w$ = number of water tiles
- $t$ = number of farm tiles
- $p$ = number of productive farm tiles
- therefore: $p$ is less or equal to 4 times $w$
	- $p <= 4w$
- we also know the total farm size 
	- $9 × 9 = 81$
- therefore: $p$ cannot be larger than total minus $w$
	- $p <= 81 - w$
- combining
	- $p <= \min(4w, 81-w)$
- maximize $w$-bound
	- $4w = 81 -w$
	- $5w = 81$
	- $w = 16.2$
- so optimum must be at $w=16$
- plug-in 
	- $p <= \min(4w, 81-w)$
	- $p <= \min(4×16, 81-16)$
	- $p <= \min(64, 65)$
- no solution can exceed
	- $p<=64$
