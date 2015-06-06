import subprocess, os

class Audio_Output():
    
    def __init__(self):
        
        self.looping = False
        self.loop_exec = None
        self.play_exec = None
        self.loop_file = None
        self.play_file = None

    def is_looping(self):
        return self.looping
        
    def loop(self, audio_file):
        if os.path.isfile(audio_file):
            if self.loop_file != audio_file:
                self.stop_loop()
                self.loop_exec = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-loop", "0", audio_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.loop_file = audio_file
            
    def play(self, audio_file):
        if os.path.isfile(audio_file):
            self.play_exec = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", audio_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.play_file = audio_file

    def pause_loop(self):
        if self.play_exec:
            if self.play_exec.poll() == None:
                self.play_exec.kill()
                self.looping = False
                
    def resume(self):
        if self.loop_file:
            self.loop_exec = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-loop", "{}".format(times), self.loop_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def stop_loop(self):
        if self.loop_exec:
            if self.loop_exec.poll() == None:
                self.loop_exec.kill()
                self.loop_exec = None
                self.loop_file = None
                self.looping = None
        
    def stop_play(self):
        if self.play_exec:
            if self.play_exec.poll() == None:
                self.play_exec.kill()
                self.play_exec = None
                self.play_file = None
                
    def stop_all(self):
        self.stop_loop()
        self.stop_play()