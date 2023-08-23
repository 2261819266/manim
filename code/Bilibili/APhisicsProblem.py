import array
from manimlib import *

FONT = "Noto Sans CJK SC"

class APhisicsProblem(Scene):
	def construct(self) -> None:
		play_kw = {"run_time": 2}
		_BLUE = "#66ccff"
		text_kw = {"font": FONT, "font_size": 24, "color": _BLUE}
		text_kw_48 = {"font": FONT, "font_size": 48, "color": _BLUE}

		to_isolate = [
			# "P", "v", "-", "f", "=", "m", "a", "dv", "dt", 
		]
		isolate_kw = {"isolate": to_isolate}

		introduce = Text(
			"""
		在我初三的时候，曾经遇到过一道关于恒定功率汽车启动物理题目
		并且题目还附了一张v-t的函数图像

			""", 
			**text_kw
		)

		self.play(Write(introduce), run_time = 5)
		self.play(introduce.animate.shift(UP * 3), run_time = 2)

		axes = Axes(
			x_range = (0, 2),
			y_range = (0, 8),
			axis_config = {
				"include_tip": True,
				"stroke_color": BLUE_E,
			},
		).shift(DOWN * 2 + LEFT * 1)
		axes.flip(UR)
		# axes.add_coordinate_labels()

		self.play(FadeIn(axes))

		f = lambda v : (-math.log(1 - v) - v)
		graph = axes.get_graph(f, x_range = (0, 0.9999, 0.002), color = _BLUE)
		limit_line = DashedLine(axes.coords_to_point(1, 0), axes.coords_to_point(1, 8))
		self.play(Write(graph), Write(limit_line))


		explain_the_problem = VGroup(
			Text("题目描述大概是说在前一段时间汽车做加速运动，后面一段时间做匀速运动", **text_kw),
			Text("我当时的直觉就是汽车的速度应该只会无线逼近那个最大值但是不会达到", **text_kw),
			Text("那时只会一些导数和积分的知识的我试图证明它，", **text_kw),
			Text("我认为只要求出速度或加速度的解析式再积分一下就可以了", **text_kw),
			Text("可是怎么都写不出那个解析式，那时我就以为这个函数是无解的", **text_kw),
			# **text_kw, buff = 1
		)
		 
		j = 3
		for i in explain_the_problem:
			self.play(Write(i.shift(UP * j / 2)))
			j -= 1

		self.wait(2)

		self.play(FadeOut(introduce), FadeOut(axes), FadeOut(explain_the_problem), FadeOut(limit_line), FadeOut(graph))
		self.wait()

		ask = Text("可是真的无解吗？", **text_kw_48)

		self.play(Write(ask))
		self.wait(2)
		self.play(FadeOut(ask))

		text = Text("几个月后我学习了一些微分方程相关的知识，突然发现这似乎是可以解的", font = FONT, font_size = 30, color = _BLUE)
		self.play(Write(text))
		self.wait(2)
		self.play(FadeOut(text))

		
		answers = VGroup(
			VGroup(
				Text("假设汽车的质量为m  初速度为0  功率为定值P 所受阻力恒为f", font = FONT, font_size = 35, color = _BLUE),
				Text("根据牛顿第二定律", **text_kw_48),
				Tex("\\frac{P}{v} - f = ma", **isolate_kw),
				Tex("\\frac{P - fv}{v} = m\\frac{dv}{dt}", **isolate_kw),
				Tex("dt = m\\frac{v}{P - fv}dv", **isolate_kw),
				Tex("dt = m\\frac{fv - P + P}{(P - fv)f}dv", **isolate_kw),
				Tex("dt = -\\frac{m}{f}dv + \\frac{\\frac{mP}{f}}{P - fv}dv", **isolate_kw),
				Tex("\int dt + C = \int{(-\\frac{m}{f}dv + \\frac{\\frac{mP}{f}}{P - fv}dv)}", **isolate_kw),
				Tex("t + C = -\\frac{mv}{f} - \\frac{mP}{f^2}ln(P - fv)", **isolate_kw),
				Tex("t + C = -\\frac{mv}{f} - \\frac{mP}{f^2}ln((1 - \\frac{f}{P}v)P)", **isolate_kw),
				Tex("t + C = -\\frac{mv}{f} - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)} - \\frac{mP}{f^2}lnP", **isolate_kw),
				Text("把t = 0, v = 0带入", **text_kw_48),
				Tex("0 + C = -\\frac{0m}{f} - \\frac{mP}{f^2}ln{(1 - 0\\frac{f}{P})} - \\frac{mP}{f^2}lnP", **isolate_kw),
				# Tex("0 + C = - \\frac{mP}{f^2}lnP", **isolate_kw),
				Tex("C = - \\frac{mP}{f^2}lnP", **isolate_kw),
				Text("把C回代", **text_kw_48),
				Tex("t - \\frac{mP}{f^2}lnP = -\\frac{mv}{f} - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)} - \\frac{mP}{f^2}lnP", **isolate_kw),
				Tex("t = -\\frac{m}{f}v - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)}", **isolate_kw),
			),
			VGroup(
				Text("假设汽车的质量为m  初速度为0  功率为定值P 所受阻力为kv", font = FONT, font_size = 35, color = _BLUE),
				Text("根据牛顿第二定律", **text_kw_48),
				Tex("\\frac{P}{v} - kv = ma", **isolate_kw),
				Tex("\\frac{P - kv^2}{v} = m\\frac{dv}{dt}", **isolate_kw),
				Tex("dt = m\\frac{v}{P - kv^2}{dv}", **isolate_kw),
				Tex("dt = -m\\frac{-2kv}{2k(P - kv^2)}dv", **isolate_kw),
				Tex("\int dt + C = \int -m\\frac{-2kv}{2k(P - kv^2)}dv", **isolate_kw),
				Tex("t + C = -\\frac{m}{2k}ln(P - kv^2)", **isolate_kw),
				Tex("t + C = -\\frac{m}{2k}ln(P(1 - \\frac{k}{P}v^2)", **isolate_kw),
				Tex("t + C = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2) - \\frac{m}{2k}lnP", **isolate_kw),
				Text("把t = 0, v = 0带入", **text_kw_48),
				Tex("0 + C = -\\frac{m}{2k}ln(1 - \\frac{k}{P}0^2) - \\frac{m}{2k}lnP", **isolate_kw),
				Tex("C = - \\frac{m}{2k}lnP", **isolate_kw),
				Text("把C回代", **text_kw_48),
				Tex("t - \\frac{m}{2k}lnP = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2) - \\frac{m}{2k}lnP", **isolate_kw),
				Tex("t = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2)", **isolate_kw),
				Tex("-\\frac{2k}{m}t = ln(1 - \\frac{k}{P}v^2)", **isolate_kw),
				Tex("e ^ {-\\frac{2k}{m}t} = e^{ln(1 - \\frac{k}{P}v^2)}", **isolate_kw),
				Tex("e ^ {-\\frac{2k}{m}t} = 1 - \\frac{k}{P}v^2", **isolate_kw),
				Tex("\\frac{k}{P}v^2 = 1 - e ^ {-\\frac{2k}{m}t}", **isolate_kw),
				Tex("v^2 = \\frac{P}{k}(1 - e ^ {-\\frac{2k}{m}t})", **isolate_kw),
				Tex("v = \\sqrt{\\frac{P}{k}(1 - e ^ {-\\frac{2k}{m}t})}", **isolate_kw),
				
			),

			VGroup(
				Text("假设汽车的质量为m  初速度为0  功率为定值P 所受阻力为kv^2", font = FONT, font_size = 35, color = _BLUE),
				Text("根据牛顿第二定律", **text_kw_48),
				Tex("\\frac{P}{v} - kv^2 = ma", **isolate_kw),
				Tex("\\frac{P - kv^3}{v} = m\\frac{dv}{dt}", **isolate_kw),
				Tex("dt = m\\frac{v}{P - kv^3}dv", **isolate_kw),
				Tex("dt = m\\frac{v}{(\\sqrt[3]P)^3 - (\\sqrt[3]k)^3v^3}dv", **isolate_kw),
				Tex("dt = m\\frac{3v}{3(\\sqrt[3]P - \\sqrt[3]kv)((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)}dv", **isolate_kw),
				Tex("dt = m\\frac{(\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2) - (\\sqrt[3]P - \\sqrt[3]kv)^2}{3(\\sqrt[3]P - \\sqrt[3]kv)((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)}dv", **isolate_kw),
				Tex("dt = m(-\\frac{-\\sqrt[3]k}{3\\sqrt[3]k(\\sqrt[3]P - \\sqrt[3]kv)} - \\frac{(\\sqrt[3]P - \\sqrt[3]kv)}{3((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)})dv", **isolate_kw),
				Tex("dt = m(-\\frac{-\\sqrt[3]k}{3\\sqrt[3]k(\\sqrt[3]P - \\sqrt[3]kv)} + \\frac{(\\sqrt[3]kv - \\sqrt[3]P)}{3((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)})dv", **isolate_kw),
				Tex("dt = m(-\\frac{-\\sqrt[3]k}{3\\sqrt[3]k(\\sqrt[3]P - \\sqrt[3]kv)} + \\frac{(2\\sqrt[3]kv + \\sqrt[3]P) - 3\\sqrt[3]P}{6((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)})dv", **isolate_kw),
				Tex("dt = m(-\\frac{-\\sqrt[3]k}{3\\sqrt[3]k(\\sqrt[3]P - \\sqrt[3]kv)} + \\frac{(2\\sqrt[3]kv + \\sqrt[3]P)}{6((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)} - \\frac{3\\sqrt[3]P}{6((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)})dv", **isolate_kw, font_size = 30),
				Tex("dt = m(-\\frac{-\\sqrt[3]k}{3\\sqrt[3]k(\\sqrt[3]P - \\sqrt[3]kv)} + \\frac{(2\\sqrt[3]kv + \\sqrt[3]P)}{6((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)} - \\frac{\\sqrt[3]P}{2((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)})dv", **isolate_kw, font_size = 30),
				Tex("\\int dt + C = \\int m(-\\frac{-\\sqrt[3]k}{3\\sqrt[3]k(\\sqrt[3]P - \\sqrt[3]kv)} + \\frac{(2\\sqrt[3]kv + \\sqrt[3]P)}{6((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)} - \\frac{\\sqrt[3]P}{2((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2)})dv", **isolate_kw, font_size = 30),
				Tex("t + C = -\\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P - \\sqrt[3]kv) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2 + \\sqrt[3]P\\sqrt[3]kv + (\\sqrt[3]kv)^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]kv}{\\sqrt{3}\\sqrt[3]P})", **isolate_kw, font_size = 30),
				Tex(
					"t + C = -\\frac{m}{3\\sqrt[3]k} ln(1 - \\frac{\\sqrt[3]k}{\\sqrt[3]P}v) - \\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln(1 + \\frac{\\sqrt[3]k}{\\sqrt[3]P}kv + (\\frac{\\sqrt[3]k}{\\sqrt[3]P})^2v^2) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]kv}{\\sqrt{3}\\sqrt[3]P})", 
					**isolate_kw, font_size = 20
				),
				Text("把t = 0, v = 0带入", **text_kw_48),
				Tex(
					"0 + C = -\\frac{m}{3\\sqrt[3]k} ln(1 - \\frac{\\sqrt[3]k}{\\sqrt[3]P} \\cdot 0) - \\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln(1 + \\frac{\\sqrt[3]k}{\\sqrt[3]P}\\cdot 0 + (\\frac{\\sqrt[3]k}{\\sqrt[3]P})^2\\cdot 0) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]k\\cdot 0}{\\sqrt{3}\\sqrt[3]P})", 
					**isolate_kw, font_size = 20
				),
				Tex("C = -\\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt3}{3})", **isolate_kw, font_size = 30),
				Tex("C = -\\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}\\cdot \\frac{\\pi}{6}", **isolate_kw, font_size = 30),
				Tex("C = -\\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{6\\sqrt{3}\\sqrt[3]k}\\pi", **isolate_kw, font_size = 30),
				Text("把C回代", **text_kw_48),
				Tex(
					"t - \\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{6\\sqrt{3}\\sqrt[3]k}\\pi = -\\frac{m}{3\\sqrt[3]k} ln(1 - \\frac{\\sqrt[3]k}{\\sqrt[3]P}v) - \\frac{m}{3\\sqrt[3]k} ln(\\sqrt[3]P) + \\frac{m}{6\\sqrt[3]k}ln(1 + \\frac{\\sqrt[3]k}{\\sqrt[3]P}kv + (\\frac{\\sqrt[3]k}{\\sqrt[3]P})^2v^2) + \\frac{m}{6\\sqrt[3]k}ln((\\sqrt[3]P)^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]kv}{\\sqrt{3}\\sqrt[3]P})", 
					**isolate_kw, font_size = 17
				),
				Tex(
					"t - \\frac{m}{6\\sqrt{3}\\sqrt[3]k}\\pi = -\\frac{m}{3\\sqrt[3]k} ln(1 - \\frac{\\sqrt[3]k}{\\sqrt[3]P}v) + \\frac{m}{6\\sqrt[3]k}ln(1 + \\frac{\\sqrt[3]k}{\\sqrt[3]P}kv + (\\frac{\\sqrt[3]k}{\\sqrt[3]P})^2v^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]kv}{\\sqrt{3}\\sqrt[3]P})", 
					**isolate_kw, font_size = 30
				),
				Tex(
					"t = \\frac{m}{6\\sqrt{3}\\sqrt[3]k}\\pi - \\frac{m}{3\\sqrt[3]k} ln(1 - \\frac{\\sqrt[3]k}{\\sqrt[3]P}v) + \\frac{m}{6\\sqrt[3]k}ln(1 + \\frac{\\sqrt[3]k}{\\sqrt[3]P}kv + (\\frac{\\sqrt[3]k}{\\sqrt[3]P})^2v^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]kv}{\\sqrt{3}\\sqrt[3]P})", 
					**isolate_kw, font_size = 30
				),
			)
		)

		assumes = VGroup(
			Text("首先来看一种比较简单的情况 即汽车所受的阻力为恒力f", font = FONT, font_size = 35, color = _BLUE),
			Text("如果考虑更真实的情况呢？", font = FONT, font_size = 35, color = _BLUE),			
		)

		self.play(Write(assumes[0]))
		self.play(FadeOut(assumes[0]))
		
		ans = answers[0]
		# for ans in answers:
		#	 for i in ans:
		#		 if i.__class__ == Tex:
		#			 i.set_color_by_tex_to_color_map({
		#				 "dv": PURPLE,
		#				 "dt": RED,
		#				 "v":  PURPLE,
		#				 "t":  RED,
		#				 # "P":  PINK,
		#				 # "f":  _BLUE,
		#			 })


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
					self.play(FadeOut(k1))
					self.play(FadeIn(i.shift(UP)))
				k1 = i
			self.wait()
		self.wait(3)

		# self.play(FadeOut(ans))
		self.clear()
		



		self.play(Write(assumes[1]))
		self.play(FadeOut(assumes[1]))

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
					self.play(FadeOut(k1))
					self.play(FadeIn(i.shift(UP)))
				k1 = i
			self.wait()
		self.wait(3)
		# self.play(FadeOut(answers))
		self.clear()





		ans = answers[2]

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
							k2, i, path_arc = PI / 4,
						), **play_kw
					)
				k2 = i
			else:
				if k1 and i != ans[0] and i != ans[1]:
					self.play(FadeOut(k1))
					self.play(FadeIn(i.shift(UP)))
				k1 = i
			self.wait()
		self.wait(3)

		self.clear()

		self.wait()

		draw_text = Text("最后我们来欣赏一下他们的图像", **text_kw_48)

		self.play(FadeIn(draw_text))
		self.play(FadeOut(draw_text))

		self.wait()


		pictures_text = VGroup(
			Tex("t = -\\frac{m}{f}v - \\frac{mP}{f^2}ln{(1 - \\frac{f}{P}v)}", **isolate_kw, color = RED).shift(UP * 3),
			Tex("v = \\sqrt{\\frac{P}{k}(1 - e ^ {-\\frac{2k}{m}t})} \\Leftrightarrow  t = -\\frac{m}{2k}ln(1 - \\frac{k}{P}v^2)", **isolate_kw, color = YELLOW, font_size = 40).shift(UP * 2),
			Tex(
				"t = \\frac{m}{6\\sqrt{3}\\sqrt[3]k}\\pi - \\frac{m}{3\\sqrt[3]k} ln(1 - \\frac{\\sqrt[3]k}{\\sqrt[3]P}v) + \\frac{m}{6\\sqrt[3]k}ln(1 + \\frac{\\sqrt[3]k}{\\sqrt[3]P}kv + (\\frac{\\sqrt[3]k}{\\sqrt[3]P})^2v^2) - \\frac{m}{\\sqrt{3}\\sqrt[3]k}tan^{-1}(\\frac{\\sqrt[3]P + 2\\sqrt[3]kv}{\\sqrt{3}\\sqrt[3]P})", 
				**isolate_kw, font_size = 30, color = _BLUE
			).shift(UP * 1),
		)

		transform = VGroup(
			Tex("t = - v - ln(1 - v)", **isolate_kw, color = RED).shift(UP * 3),
			Tex("v = \\sqrt{(1 - e ^ {-2t})} \\Leftrightarrow  t = -\\frac{1}{2}ln(1 - v^2)", **isolate_kw, color = YELLOW).shift(UP * 2),
			Tex(
				"t = \\frac{1}{6\\sqrt{3}}\\pi - \\frac{1}{3} ln(1 - v) + \\frac{1}{6}ln(1 + v + v^2) - \\frac{1}{\\sqrt{3}}tan^{-1}(\\frac{1 + 2v}{\\sqrt{3}})", 
				**isolate_kw, color = _BLUE
			).shift(UP * 1),
		)

		transform_text = Text("我们假设m, P, f, k的值均为1 为了方便观察 以下的图像均被沿竖直方向拉伸了4倍(横轴为t 纵轴为v)", font = FONT, font_size = 25, color = _BLUE)

		self.play(Write(transform_text))
		self.wait()
		self.play(FadeOut(transform_text))
		self.wait()

		self.play(FadeIn(pictures_text))

		for i in range(0, 3):
			self.play(TransformMatchingTex(pictures_text[i], transform[i]))



		pictures = VGroup(

		)
		axes_draw = Axes(
			x_range = (0, 4),
			y_range = (0, 8),
			axis_config = {
				"include_tip": True,
				"stroke_color": WHITE,
			},
		).shift(DOWN * 1.5)
		axes_draw.flip(UR)



		self.play(FadeIn(axes_draw))

		log = math.log
		sqrt_3 = math.sqrt(3)

		k = 4
		limit_line = DashedLine(axes_draw.coords_to_point(k, 0), axes_draw.coords_to_point(k, 8))
		self.play(Write(limit_line))

		
		functions = [
			lambda v : (-log(1 - v) - v),
			lambda v : (-0.5 * log(1 - v ** 2)),
			lambda v : (1.0 / 6 / sqrt_3 * PI
				- 1.0 / 3 * log(1 - v) 
				+ 1.0 / 6 * log(1 + v + v ** 2) 
				- 1.0 / sqrt_3 * math.atan(((1 + 2 * v) / sqrt_3))),
		]

		for i in range(0, 3):
			functions_graph = axes_draw.get_graph(
				functions[i], 
				x_range = (0, [0.9999, 0.9999999, 0.9999999999][i], 0.002), 
				color = [RED, YELLOW, _BLUE][i]
			).stretch(factor = k, dim = 1, about_edge = DOWN)
			self.play(Write(functions_graph))

