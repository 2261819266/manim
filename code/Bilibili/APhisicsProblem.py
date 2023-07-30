import array
from manimlib import *

FONT = "Noto Sans CJK SC"

class APhisicsProblem(Scene):
    def construct(self) -> None:

        # introduce = Text(
        #     """
        # 在我初三的时候，曾经遇到过一道关于恒定功率汽车启动物理题目
        # 并且题目还附了一张v-t的函数图像

        #     """, 
        #     font = FONT, font_size = 24, color = BLUE
        # )

        # self.play(Write(introduce), run_time = 5)
        # self.play(introduce.animate.shift(UP * 3), run_time = 2)

        # axes = Axes(
        #     x_range = (0, 2),
        #     y_range = (0, 8),
        #     axis_config = {
        #         "include_tip": True,
        #         "stroke_color": BLUE_E,
        #     },
        # ).shift(DOWN * 2 + LEFT * 1)
        # axes.flip(UR)
        # axes.add_coordinate_labels()

        # self.play(FadeIn(axes))

        # f = lambda v : (-math.log(1 - v) - v)
        # graph = axes.get_graph(f, x_range = (0, 0.9999, 0.002), color = BLUE)
        # limit_line = DashedLine(axes.coords_to_point(1, 0), axes.coords_to_point(1, 8))
        # self.play(Write(graph), Write(limit_line))


        # explain_the_problem = VGroup(
        #     Text("题目描述大概是说在前一段时间汽车做加速运动，后面一段时间做匀速运动", font = FONT, font_size = 24, color = BLUE),
        #     Text("我当时的直觉就是汽车的速度应该只会无线逼近那个最大值但是不会达到", font = FONT, font_size = 24, color = BLUE),
        #     Text("那时只会一些导数和积分的知识的我试图证明它，", font = FONT, font_size = 24, color = BLUE),
        #     Text("我认为只要求出速度或加速度的解析式再积分一下就可以了", font = FONT, font_size = 24, color = BLUE),
        #     Text("可是怎么都写不出那个解析式，那时我就以为这个函数是无解的", font = FONT, font_size = 24, color = BLUE),
        #     # font = FONT, font_size = 24, color = BLUE, buff = 1
        # )

        # j = 3
        # for i in explain_the_problem:
        #     self.play(Write(i.shift(UP * j / 2 )))
        #     j -= 1

        # self.play(FadeOut(introduce), FadeOut(axes), FadeOut(explain_the_problem), FadeOut(limit_line), FadeOut(graph))
        # self.wait()

        # ask = Text("可是真的无解吗？", font = "Noto Sans CJK SC", font_size = 48, color = BLUE)

        # self.play(Write(ask))
        # self.wait(2)
        # self.play(FadeOut(ask))

        # text = Text("几个月后我学习了一些微分方程相关的知识，突然发现这似乎是可以解的", font = "Noto Sans CJK SC", font_size = 30, color = BLUE)
        # self.play(Write(text))
        # self.wait(2)
        # self.play(FadeOut(text))

        to_isolate = [
            "P", "v", "-", "f", "=", "m", "a", "dv", "dt", 
        ]
        answers = VGroup(
            VGroup(
                Text("假设汽车的质量为m  初速度为0  功率为定值P 所受阻力恒为f", font = "Noto Sans CJK SC", font_size = 35, color = BLUE),
                Text("根据牛顿第二定律", font = "Noto Sans CJK SC", font_size = 48, color = BLUE),
                Tex("\\frac{P}{v} - f = ma", isolate = to_isolate),
                Tex("\\frac{P - fv}{v} = m\\frac{dv}{dt}", isolate = to_isolate),
                Tex("dt = m\\frac{v}{P - fv}dv", isolate = to_isolate),
                Tex("dt = m\\frac{fv - P + P}{(P - fv)f}dv", isolate = to_isolate),
                Tex("dt = -\\frac{m}{f}dv + \\frac{\\frac{mP}{f}}{P - fv}dv", isolate = to_isolate),
                Tex("\int dt + C = \int{(-\\frac{m}{f}dv + \\frac{\\frac{mP}{f}}{P - fv}dv)}", isolate = to_isolate),
                Tex("t + C = -\\frac{mv}{f} - \\frac{mP}{f^2}ln(P - fv)", isolate = to_isolate),
                Tex("t + C = -\\frac{mv}{f} - \\frac{mP}{f^2}ln((1 - \\frac{f}{P}v)P)", isolate = to_isolate),
                Tex("t + C = -\\frac{mv}{f} - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)} - \\frac{mP}{f^2}lnP", isolate = to_isolate),
                Text("把t = 0, v = 0带入", font = "Noto Sans CJK SC", font_size = 48, color = BLUE),
                Tex("0 + C = -\\frac{0m}{f} - \\frac{mP}{f^2}ln{(1 - 0\\frac{f}{P})} - \\frac{mP}{f^2}lnP", isolate = to_isolate),
                # Tex("0 + C = - \\frac{mP}{f^2}lnP", isolate = to_isolate),
                Tex("C = - \\frac{mP}{f^2}lnP", isolate = to_isolate),
                Text("把C回代", font = "Noto Sans CJK SC", font_size = 48, color = BLUE),
                Tex("t - \\frac{mP}{f^2}lnP = -\\frac{mv}{f} - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)} - \\frac{mP}{f^2}lnP", isolate = to_isolate),
                Tex("t = -\\frac{m}{f}v - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)}", isolate = to_isolate),
            ),
            VGroup(
                Text("假设汽车的质量为m  初速度为0  功率为定值P 所受阻力为kv", font = "Noto Sans CJK SC", font_size = 35, color = BLUE),
                Text("根据牛顿第二定律", font = "Noto Sans CJK SC", font_size = 48, color = BLUE),
                Tex("\\frac{P}{v} - kv = ma", isolate = to_isolate),
                Tex("\\frac{P - kv^2}{v} = m\\frac{dv}{dt}", isolate = to_isolate),
                Tex("dt = m\\frac{v}{P - kv^2}{dv}", isolate = to_isolate),
                Tex("dt = -m\\frac{-2kv}{2k(P - kv^2)}dv", isolate = to_isolate),
                Tex("\int dt + C = \int -m\\frac{-2kv}{2k(P - kv^2)}dv", isolate = to_isolate),
                Tex("t + C = -\\frac{m}{2k}ln(P - kv^2)", isolate = to_isolate),
                Tex("t + C = -\\frac{m}{2k}ln(P(1 - \\frac{k}{P}v^2)", isolate = to_isolate),
                Tex("t + C = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2) - \\frac{m}{2k}lnP", isolate = to_isolate),
                Text("把t = 0, v = 0带入", font = "Noto Sans CJK SC", font_size = 48, color = BLUE),
                Tex("0 + C = -\\frac{m}{2k}ln(1 - \\frac{k}{P}0^2) - \\frac{m}{2k}lnP", isolate = to_isolate),
                Tex("C = - \\frac{m}{2k}lnP", isolate = to_isolate),
                Text("把C回代", font = "Noto Sans CJK SC", font_size = 48, color = BLUE),
                Tex("t - \\frac{m}{2k}lnP = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2) - \\frac{m}{2k}lnP", isolate = to_isolate),
                Tex("t = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2)", isolate = to_isolate),
                Tex("-\\frac{2k}{m}t = ln(1 - \\frac{k}{P}v^2)", isolate = to_isolate),
                Tex("e ^ {-\\frac{2k}{m}t} = e^{ln(1 - \\frac{k}{P}v^2)}", isolate = to_isolate),
                Tex("e ^ {-\\frac{2k}{m}t} = 1 - \\frac{k}{P}v^2", isolate = to_isolate),
                Tex("\\frac{k}{P}v^2 = 1 - e ^ {-\\frac{2k}{m}t}", isolate = to_isolate),
                Tex("v^2 = \\frac{P}{k}(1 - e ^ {-\\frac{2k}{m}t})", isolate = to_isolate),
                Tex("v = \\sqrt{\\frac{P}{k}(1 - e ^ {-\\frac{2k}{m}t})}", isolate = to_isolate),
                
            )
        )
        
        ans = answers[0]
        play_kw = {"run_time": 3}
        # for i in ans:
        #     if i.__class__ == Tex:
        #         i.set_color_by_tex_to_color_map({
        #             "{dv}": PURPLE,
        #             "{dt}": RED,
        #             "{v}":  PURPLE,
        #             "{t}":  RED,
        #             # "P":  PINK,
        #             # "f":  BLUE,
        #         })


        # self.play(Write(ans[0]))
        # self.play(ans[0].animate.shift(UP * 3))

        # self.play(Write(ans[1].shift(UP)))
        # self.play(Write(ans[2]))
        # self.play(
        #     TransformMatchingTex(
        #         ans[2], ans[3],
        #         path_arc = PI / 2,
        #     )
        # )
        # self.play(
        #     TransformMatchingTex(
        #         ans[3], ans[4],
        #         path_arc = PI / 2,
        #     )
        # )
        # k1 = ans[1]
        # k2 = 0
        # for i in ans:
        #     if i.__class__ == Tex:
        #         if k2:
        #             self.play(
        #                 TransformMatchingTex(
        #                     k2, i, path_arc = PI / 2,
        #                 ), **play_kw
        #             )
        #         k2 = i
        #     else:
        #         if k1 and i != ans[0] and i != ans[1]:
        #             # self.play(
        #             #     TransformMatchingTex(
        #             #         k1, i.shift(UP)
        #             #     ), **play_kw
        #             # )
        #             self.play(FadeOut(k1))
        #             self.play(FadeIn(i.shift(UP)))
        #         k1 = i
        #     self.wait()
        # self.wait(5)

        # self.play(FadeOut(ans))

        ans = answers[1]

        self.play(Write(ans[0]))
        self.play(ans[0].animate.shift(UP * 3))

        self.play(Write(ans[1].shift(UP)))
        self.play(Write(ans[2]))

        k1 = ans[1]
        k2 = 0

        for i in ans:
            if i.__class__ == Tex:
                if k2:
                    self.play(
                        TransformMatchingTex(
                            k2, i, path_arc = PI / 2,
                        ), **play_kw
                    )
                k2 = i
            else:
                if k1 and i != ans[0] and i != ans[1]:
                    # self.play(
                    #     TransformMatchingTex(
                    #         k1, i.shift(UP)
                    #     ), **play_kw
                    # )
                    self.play(FadeOut(k1))
                    self.play(FadeIn(i.shift(UP)))
                k1 = i
            self.wait()
        self.wait(5)
