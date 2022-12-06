from manim import *

class SA_Practice_Problem(ThreeDScene):
    
    def construct(self):
        text = VGroup(
            Tex(r"$S = \int_{0}^{2}2\pi x^{3} \sqrt{1+(\frac{dy}{dx})^{2}}dx$"),
            Tex(r"$S = \int_{0}^{2}2\pi x^{3} \sqrt{1+(3x^{2})^{2}}dx$"),
            Tex(r"$S = 2\pi\int_{0}^{2}x^{3}(1+9x^{4})^{1/2}dx$"),
            Tex(r"$u=1+9x^4, du=36x^{3}dx$"),
            Tex(r"$S=\frac{2}{36}\pi \int_{1}^{145}u^{1/2}du$"),
            Tex(r"$S=\frac{2\pi}{36}\left[\ \frac{2}{3}u^{3/2} \right]_1^{145}$"),
            Tex(r"$S \approx 203 \ units^{2}$"),
        )
        text.arrange(DOWN)
        text.to_edge(UP)
        self.play(Write(text))






