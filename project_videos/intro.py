from manim import DOWN, LEFT, UR, Scene, StreamLines, Tex, Write
import numpy as np


class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        title = Tex("Surfaces of Revolution")
        names = Tex("Akhil Datla and Aditya Pawar").next_to(title, DOWN, buff=0.5)
        self.play(Write(title))
        self.play(Write(names))
        self.wait(10)
