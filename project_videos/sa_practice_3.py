from manim import UP, ThreeDScene, Tex, DOWN, Write, SurroundingRectangle, Create


class SA_Practice_Problem(ThreeDScene):
    def construct(self):
        step1 = (
            Tex(r"$y=x^2 \rightarrow x=\sqrt{y}$")
            .move_to(UP)
            .shift(UP * 2)
        )
        step2 = Tex(r"$S=\int_{0}^{3}2\pi\sqrt{y}\sqrt{1+(\frac{1}{2\sqrt{y}})^2}dy$").next_to(
            step1, DOWN, buff=0.2
        )
        step3 = Tex(r"$S=\pi\int_{0}^{3}\sqrt{4y+1}dy$").next_to(
            step2, DOWN, buff=0.2
        )

        step4 = Tex(r"$u=4y+1$").next_to(step3, DOWN, buff=0.2)

        step5 = Tex(r"$S=\frac{\pi}{4}\int_{1}^{13}u^{1/2}du$").next_to(
            step4, DOWN, buff=0.2
        )

        step6 = Tex(
            r"$\frac{\pi}{6}[(13)^{3/2}-1]$"
        ).next_to(step5, DOWN, buff=0.2)

        step7 = Tex(r"$S \approx 24 \ units^{2}$").next_to(step6, DOWN, buff=0.2)

        box = SurroundingRectangle(step7, buff=0.1)

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
        self.wait()
        self.play(Create(box), run_time=5)
