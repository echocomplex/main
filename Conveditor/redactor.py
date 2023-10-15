"""

REDACTOR FILE FOR Conveditor - Видео и Аудио Редактор (Telegram Bot) - https://t.me/ConveditorMainBot (@ConveditorMainBot)
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)

"""


""" IMPORTS """
from moviepy.editor import *;
from moviepy.audio.fx.volumex import volumex;
import random;
import numpy as np;
import shutil;


""" VIDEO REDACTOR """
class Video:
    def __init__ (self) -> None:
        pass;

    """ CONCATENATE VIDEOS """
    def concatenate (self, src1: str, src2: str) -> str:
        try:
            clip_1 = VideoFileClip(src1);
            clip_2 = VideoFileClip(src2);
            final_clip = concatenate_videoclips([clip_1, clip_2]);
            src3 = f"videos/Conveditor_render_{random.randint(1000, 9999)}.mp4";
            final_clip.write_videofile(src3);
            return src3;
        except Exception:
            return "BAD";

    """ REMOVE AUDIO """
    def rmaudio (self, src1: str) -> str:
        try:
            clip = VideoFileClip(src1);
            final_clip = clip.without_audio();
            src2 = f"videos/Conveditor_render_{random.randint(1000, 9999)}.mp4";
            final_clip.write_videofile(src2);
            return src2;
        except Exception:
            return "BAD";

    """ GET AUDIO FROM VIDEO """
    def get_au (self, src1: str) -> str:
        try:
            final_clip = AudioFileClip(src1);
            src2 = f"music/Conveditor_render_{random.randint(1000, 9999)}.mp3";
            final_clip.write_audiofile(src2);
            return src2;
        except Exception:
            return "BAD";

    """ EXTRACT FRAMES FROM VIDEO """
    def extract_frames (self, src1: str) -> str:
        try:
            clip = VideoFileClip(src1);
            step = 1 / clip.fps;
            for current_duration in np.arange(0, clip.duration, step):
                src2 = f"photos/Conveditor_render_{str(current_duration)}.jpg";
                clip.save_frame(src2, current_duration);
            shutil.make_archive("Conveditor_render", "zip", "photos/");
            return "Conveditor_render.zip";
        except Exception:
            return "BAD";

    """ CUT VIDEO """
    def cut (self, src1: str, time1: int, time2: int) -> str:
        try:
            clip = VideoFileClip(src1);
            final_clip = clip.subclip(time1, time2);
            src2 = f"videos/Conveditor_render_{random.randint(1000, 9999)}.mp4";
            final_clip.write_videofile(src2);
            return src2;
        except Exception:
            return "BAD";

    """ CHANGE VIDEO VOLUME """
    def change_volume (self, src1: int, volume: float) -> str:
        try:
            clip = VideoFileClip(src1);
            final_clip = clip.volumex(volume);
            src2 = f"videos/Conveditor_render_{random.randint(1000, 9999)}.mp4";
            final_clip.write_videofile(src2);
            return src2;
        except Exception:
            return "BAD";

    """ ADD AUDIO TO VIDEO """
    def addaudio (self, src1: str, src2: str) -> str:
        try:
            clip = VideoFileClip(src1);
            mus_clip_2 = AudioFileClip(src2);
            try:
                clip_2 = CompositeAudioClip([clip.audio, mus_clip_2]);
            except Exception:
                pass;
            try:
                final_audio = clip_2.subclip(0, clip.duration);
                final_clip = clip.set_audio(final_audio);
            except Exception:
                final_audio = mus_clip_2.subclip(0, clip.duration);
                final_clip = clip.set_audio(final_audio);
            src3 = f"videos/Conveditor_render_{random.randint(1000, 9999)}.mp4";
            final_clip.write_videofile(src3);
            return src3;
        except Exception:
            return "BAD";


""" AUDIO REDACTOR """
class Audio:
    def __init__ (self) -> None:
        pass

    """ CONCATENATE AUDIO """
    def concatenate (self, src1: str, src2: str) -> str:
        try:
            clip_1 = AudioFileClip(src1);
            clip_2 = AudioFileClip(src2);
            final_clip = concatenate_audioclips([clip_1, clip_2]);
            src3 = f"music/Conveditor_render_{random.randint(1000, 9999)}.mp3";
            final_clip.write_audiofile(src3);
            return src3;
        except Exception:
            return "BAD";

    """ CUT AUDIO """
    def cut (self, src1: str, time1: int, time2: int) -> str:
        try:
            clip = AudioFileClip(src1);
            final_clip = clip.subclip(time1, time2);
            src2 = f"music/Conveditor_render_{random.randint(1000, 9999)}.mp3";
            final_clip.write_audiofile(src2);
            return src2;
        except Exception:
            return "BAD";

    """ CHANGE AUDIO VOLUME """
    def change_volume (self, src1: int, volume: float) -> str:
        try:
            clip = AudioFileClip(src1);
            final_clip = clip.fx(volumex, volume);
            src2 = f"music/Conveditor_render_{random.randint(1000, 9999)}.mp3";
            final_clip.write_audiofile(src2);
            return src2;
        except Exception:
            return "BAD";
