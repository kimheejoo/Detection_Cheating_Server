from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    '''학생 정보와 결과'''
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.Integer)
    name = db.Column(db.String(10))
    video_path = db.Column(db.String(50))
    packet_path = db.Column(db.String(50))
    audio_path = db.Column(db.String(50))
    audio_img_path = db.Column(db.String(50))
    audio_messages = db.Column(db.Text())
    audio_playtime = db.Column(db.Integer)
    state = db.Column(db.String(10), default="notyet")
    reason = db.Column(db.Text())
    network_result = db.Column(db.String(200))
    audio_result = db.Column(db.String(500))
    eye_result = db.Column(db.String(100))
    eye_ratio_center = db.Column(db.Integer)
    eye_ratio_blink = db.Column(db.Integer)
    eye_ratio_left = db.Column(db.Integer)
    eye_ratio_right = db.Column(db.Integer)
    time_range = db.Column(db.String(100))
    

    @property
    def serialize(self):
        return {
            "id": self.id,
            "student_number": self.student_number,
            "name": self.name,
            "video_path": self.video_path,
            "packet_path": self.packet_path,
            "audio_path": self.audio_path,
            "audio_img_path": self.audio_img_path,
            "audio_messages": self.audio_messages,
            "audio_playtime": self.audio_playtime,
            "audio_img_path": self.audio_img_path,
            "state": self.state,
            "reason": self.reason,
            "network_result": self.network_result,
            "audio_result": self.audio_result,
            "eye_result": self.eye_result,
            "eye_ratio_center": self.eye_ratio_center,
            "eye_ratio_blink": self.eye_ratio_blink,
            "eye_ratio_left": self.eye_ratio_left,
            "eye_ratio_right": self.eye_ratio_right,
            "time_range": self.time_range
        }

        