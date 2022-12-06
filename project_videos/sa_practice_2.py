from manim import UP, ThreeDScene, Tex, DOWN, Write


class SA_Practice_Problem(ThreeDScene):
    def construct(self):
        step1 = (
            Tex(r"$S = \int_{0}^{2}2\pi x^{3} \sqrt{1+(\frac{dy}{dx})^{2}}dx$")
            .move_to(UP)
            .shift(UP * 2)
        )
        step2 = Tex(r"$S = \int_{0}^{2}2\pi x^{3} \sqrt{1+(3x^{2})^{2}}dx$").next_to(
            step1, DOWN, buff=0.2
        )
        step3 = Tex(r"$S = 2\pi\int_{0}^{2}x^{3}(1+9x^{4})^{1/2}dx$").next_to(
            step2, DOWN, buff=0.2
        )

        step4 = Tex(r"$u=1+9x^4, du=36x^{3}dx$").next_to(step3, DOWN, buff=0.2)

        step5 = Tex(r"$S=\frac{2}{36}\pi \int_{1}^{145}u^{1/2}du$").next_to(
            step4, DOWN, buff=0.2
        )

        step6 = Tex(
            r"$S=\frac{2\pi}{36}\left[\ \frac{2}{3}u^{3/2} \right]_1^{145}$"
        ).next_to(step5, DOWN, buff=0.2)

        step7 = Tex(r"$S \approx 203 \ units^{2}$").next_to(step6, DOWN, buff=0.2)

        self.play(Write(step1))
        self.wait()
        self.play(Write(step2))
        self.wait()
        self.play(Write(step3))
        self.wait()
        self.play(Write(step4))
        self.wait()
        self.play(Write(step5))
        self.wait()
        self.play(Write(step6))
        self.wait()
        self.play(Write(step7))
