from typing_extensions import runtime
from manimlib import *
from sympy import isolate

class TexTrans(Scene):
	def construct(self) -> None:
		ch = ["B", "C", "=", "(", ")"]
		lines = VGroup(
			# Tex("A^2+B^2=C^2"),
			# Tex("A^2=C^2-B^2"),
			Tex("A^2", "+", "B^2", "=", "C^2"),
			Tex("A^2", "=", "C^2", "-", "B^2"),
			Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *ch]),
			# Tex("A = \\sqrt{")
		)

		lines.arrange(DOWN, buff = LARGE_BUFF)
		for i in lines:
			i.set_color_by_tex_to_color_map({
				"A": BLUE, 
				"B": TEAL,
				"C": GREEN,
			})

		self.add(lines[0])

		self.play(
			TransformMatchingTex(
				lines[0].copy(), lines[1],
				path_arc=90 * DEGREES,
			),
			run_time = 2
		)

		self.play(
			TransformMatchingTex(lines[1].copy(), lines[2]),
			run_time = 2,
		)