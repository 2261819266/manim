from typing_extensions import runtime
from manimlib import * # type: ignore

class SolveEquation(Scene) :
    def construct(self) -> None:
        ch = [ 'a', 'b', 'c', 'x', ]
        lines = VGroup(
            Tex("ax^2 + bx + c = 0", isolate = ["x^2", *ch, "0"]),
            # Tex("x^2 + $\\frac{b}{a}$ x + $\\frac{c}{a}$ = 0", isolate = ["x^2", *ch]),
            Tex("x^2", "+", "\\frac{b}{a}", "x", "+", "\\frac{c}{a}", "=", "0"),
            Tex("x^2", "+", "\\frac{b}{a}", "x", "=", "-", "\\frac{c}{a}"),
            Tex("x^2", "+", "2", "\\cdot", "\\frac{b}{2a}", "x", "+", "\\left(", 
            "\\frac{b}{2a}", "\\right)", "^", "2", "=", "\\frac{b^2}{4a^2}", "-", "\\frac{c}{a}"),
            Tex("\\left(", "x", "+", "\\frac{b}{2a}", "\\right)^2", "=", "{", 
            "{", "b^2", "-", "4ac", "}", "\\over", "{", "4a^2", "}}"),
            # Tex("\\therefore 当", "b^2")
        )
        lines.arrange(DOWN, buff = 0.5)
        for i in lines:
            i.set_color_by_tex_to_color_map( # type: ignore
                dict([(i, RED) for i in "0123456789abc"])
            )
            i.set_color_by_tex_to_color_map( # type: ignore
                dict([(i, '#66ccff') for i in "x"])
            )
            i.set_color_by_tex_to_color_map( # type: ignore
                dict([(i, YELLOW) for i in "+-=()"])
            )
            # i.set_color_by_tex_to_color_map( # type: ignore
            #     "": PURPLE,
            # )
        self.add(lines[0])
        # self.play(TransformMatchingTex(lines[0].copy(), lines[1], path_arc = PI / 2), run_time = 2)
        # self.play(TransformMatchingTex(lines[1].copy(), lines[2], path_arc = PI / 2), run_time = 2)
        for i in range(0, lines.__len__() - 1):
            self.play(TransformMatchingTex(lines[i].copy(), lines[i + 1], path_arc = PI / 2), run_time = 1)
            
        