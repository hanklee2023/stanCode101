"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow

# Constant for Window
WIDTH = 654
HEIGHT = 652


def main():
    window = GWindow(WIDTH, HEIGHT, title="My Cute Gog can code Python")
    window.color = 'ghostwhite'

    # Lift hand white
    left_hand = GPolygon()
    left_hand.add_vertex((100, 380))
    left_hand.add_vertex((32, 424))
    left_hand.add_vertex((31, 433))
    left_hand.add_vertex((30, 443))
    left_hand.add_vertex((31, 453))
    left_hand.add_vertex((32, 462))
    left_hand.add_vertex((125, 462))
    left_hand.filled = True
    left_hand.fill_color = 'white'
    left_hand.color = 'burlywood'

    # Lift hand moccasin
    left_hand_c = GPolygon()
    left_hand_c.add_vertex((100, 380))
    left_hand_c.add_vertex((95, 390))
    left_hand_c.add_vertex((90, 421))
    left_hand_c.add_vertex((97, 440))
    left_hand_c.add_vertex((104, 450))
    left_hand_c.add_vertex((125, 462))
    left_hand_c.filled = True
    left_hand_c.fill_color = 'navajowhite'
    left_hand_c.color = 'burlywood'

    # right hand white
    right_hand = GPolygon()
    right_hand.add_vertex((WIDTH - 100, 380))
    right_hand.add_vertex((WIDTH - 32, 424))
    right_hand.add_vertex((WIDTH - 31, 433))
    right_hand.add_vertex((WIDTH - 30, 443))
    right_hand.add_vertex((WIDTH - 31, 453))
    right_hand.add_vertex((WIDTH - 32, 462))
    right_hand.add_vertex((WIDTH- 125, 462))
    right_hand.filled = True
    right_hand.fill_color = 'white'
    right_hand.color = 'burlywood'

    # right hand moccasin
    right_hand_c = GPolygon()
    right_hand_c.add_vertex((WIDTH - 100, 380))
    right_hand_c.add_vertex((WIDTH - 95, 390))
    right_hand_c.add_vertex((WIDTH - 90, 421))
    right_hand_c.add_vertex((WIDTH - 97, 440))
    right_hand_c.add_vertex((WIDTH - 104, 450))
    right_hand_c.add_vertex((WIDTH - 125, 462))
    right_hand_c.filled = True
    right_hand_c.fill_color = 'navajowhite'
    right_hand_c.color = 'burlywood'

    # Big Face
    face = GOval(454, 418, x=100, y=157)
    face.filled = True
    face.fill_color = 'navajowhite'
    face.color = 'burlywood'

    # Small Face
    small_face = GOval(204, 195, x=225, y=380)
    small_face.color = 'burlywood'

    # Face Lower Part
    face_lower_left = GPolygon()
    face_lower_left.add_vertex((108, 420))
    face_lower_left.add_vertex((180, 417))
    face_lower_left.add_vertex((243, 423))
    face_lower_left.add_vertex((327, 445))
    face_lower_left.add_vertex((327, 575))
    face_lower_left.add_vertex((272, 570))
    face_lower_left.add_vertex((218, 550))
    face_lower_left.add_vertex((190, 533))
    face_lower_left.add_vertex((163, 510))
    face_lower_left.add_vertex((136, 480))
    face_lower_left.add_vertex((122, 460))
    face_lower_left.filled = True
    face_lower_left.fill_color = 'white'
    face_lower_left.color = 'burlywood'

    face_lower_right = GPolygon()
    face_lower_right.add_vertex((WIDTH - 108, 420))
    face_lower_right.add_vertex((WIDTH - 180, 417))
    face_lower_right.add_vertex((WIDTH - 243, 423))
    face_lower_right.add_vertex((WIDTH - 327, 445))
    face_lower_right.add_vertex((WIDTH - 327, 575))
    face_lower_right.add_vertex((WIDTH - 272, 570))
    face_lower_right.add_vertex((WIDTH - 218, 550))
    face_lower_right.add_vertex((WIDTH - 190, 533))
    face_lower_right.add_vertex((WIDTH - 163, 510))
    face_lower_right.add_vertex((WIDTH - 136, 480))
    face_lower_right.add_vertex((WIDTH - 122, 460))
    face_lower_right.filled = True
    face_lower_right.fill_color = 'white'
    face_lower_right.color = 'burlywood'

    # Nose
    nose = GOval(76, 80, x=289, y=410)
    nose.filled = True
    nose.fill_color = 'black'
    nose.color = 'burlywood'

    # Beard
    # Beard Vertical
    bv = GRect(4, 25, x=325, y=490)
    bv.filled = True
    bv.fill_color = 'black'
    bv.color = 'black'

    # Beard left
    bf = GPolygon()
    bf.add_vertex((327, 515))
    bf.add_vertex((331, 515))
    bf.add_vertex((400, 525))
    bf.add_vertex((395, 527))
    bf.add_vertex((327, 517))
    bf.filled = True
    bf.fill_color = 'black'

    # Beard right
    br = GPolygon()
    br.add_vertex((WIDTH - 327, 515))
    br.add_vertex((WIDTH - 331, 515))
    br.add_vertex((WIDTH - 400, 525))
    br.add_vertex((WIDTH - 395, 527))
    br.add_vertex((WIDTH - 327, 517))
    br.filled = True
    br.fill_color = 'black'

    # Beard Additional Line
    ba = GLine(327, 518, 327, 575)
    ba.color = 'moccasin'

    # Eyes
    left_eye = GOval(50, 40, x=235, y=238)
    left_eye.filled = True
    left_eye.fill_color = 'white'
    left_eye.color = 'moccasin'

    right_eye = GOval(50, 40, x=WIDTH - 235 - 50, y=238)
    right_eye.filled = True
    right_eye.fill_color = 'white'
    right_eye.color = 'moccasin'

    # Face Line
    left_line1 = GLine(250, 413, 195, 310)
    left_line1.color = 'burlywood'
    left_line2 = GLine(195, 310, 196, 220)
    left_line2.color = 'burlywood'
    left_line3 = GLine(196, 220, 198, 194)
    left_line3.color = 'burlywood'

    right_line1 = GLine(WIDTH - 250, 413, WIDTH - 195, 310)
    right_line1.color = 'burlywood'
    right_line2 = GLine(WIDTH - 195, 310, WIDTH - 196, 220)
    right_line2.color = 'burlywood'
    right_line3 = GLine(WIDTH - 196, 220, WIDTH - 198, 194)
    right_line3.color = 'burlywood'

    # Eyebrow
    # Left eyebrow for black
    left_eyebrow_b = GArc(60, 60, 0, -180, x=140, y=340)
    left_eyebrow_b.filled = True
    left_eyebrow_b.fill_color = 'black'

    # Left eyebrow for moccasin
    left_eyebrow_m = GArc(40, 33, 0, -180, x=150, y=346)
    left_eyebrow_m.filled = True
    left_eyebrow_m.fill_color = 'moccasin'
    left_eyebrow_m.color = 'moccasin'

    # right eyebrow for black
    right_eyebrow_b = GArc(60, 60, 0, -180, x=WIDTH - 140 - 60, y=340)
    right_eyebrow_b.filled = True
    right_eyebrow_b.fill_color = 'black'

    # right eyebrow for moccasin
    right_eyebrow_m = GArc(40, 33, 0, -180, x=WIDTH - 150 - 40, y=346)
    right_eyebrow_m.filled = True
    right_eyebrow_m.fill_color = 'moccasin'
    right_eyebrow_m.color = 'moccasin'

    # Ears
    # Left Ear for Black
    left_ear_b = GPolygon()
    left_ear_b.add_vertex((130, 263))
    left_ear_b.add_vertex((128, 250))
    left_ear_b.add_vertex((150, 90))
    left_ear_b.add_vertex((175, 110))
    left_ear_b.add_vertex((200, 125))
    left_ear_b.add_vertex((235, 175))
    left_ear_b.add_vertex((200, 192))
    left_ear_b.add_vertex((190, 200))
    left_ear_b.filled = True
    left_ear_b.fill_color = 'white'
    left_ear_b.color = 'burlywood'

    # Left Ear for moccasin
    left_ear_s = GPolygon()
    left_ear_s.add_vertex((150, 90))
    left_ear_s.add_vertex((160, 92))
    left_ear_s.add_vertex((168, 100))
    left_ear_s.add_vertex((175, 105))
    left_ear_s.add_vertex((185, 112))
    left_ear_s.add_vertex((190, 117))
    left_ear_s.add_vertex((200, 125))
    left_ear_s.add_vertex((210, 140))
    left_ear_s.add_vertex((220, 155))
    left_ear_s.add_vertex((225, 162))
    left_ear_s.add_vertex((235, 175))
    left_ear_s.add_vertex((210, 186))
    left_ear_s.filled = True
    left_ear_s.fill_color = 'moccasin'
    left_ear_s.color = 'burlywood'

    # Right Ear for Black
    right_ear_b = GPolygon()
    right_ear_b.add_vertex((WIDTH - 130, 263))
    right_ear_b.add_vertex((WIDTH - 128, 250))
    right_ear_b.add_vertex((WIDTH - 150, 90))
    right_ear_b.add_vertex((WIDTH - 175, 110))
    right_ear_b.add_vertex((WIDTH - 200, 125))
    right_ear_b.add_vertex((WIDTH - 235, 175))
    right_ear_b.add_vertex((WIDTH - 200, 192))
    right_ear_b.add_vertex((WIDTH - 190, 200))
    right_ear_b.filled = True
    right_ear_b.fill_color = 'white'
    right_ear_b.color = 'burlywood'

    # Right Ear for moccasin
    right_ear_s = GPolygon()
    right_ear_s.add_vertex((WIDTH - 150, 90))
    right_ear_s.add_vertex((WIDTH - 160, 92))
    right_ear_s.add_vertex((WIDTH - 168, 100))
    right_ear_s.add_vertex((WIDTH - 175, 105))
    right_ear_s.add_vertex((WIDTH - 185, 112))
    right_ear_s.add_vertex((WIDTH - 190, 117))
    right_ear_s.add_vertex((WIDTH - 200, 125))
    right_ear_s.add_vertex((WIDTH - 210, 140))
    right_ear_s.add_vertex((WIDTH - 220, 155))
    right_ear_s.add_vertex((WIDTH - 225, 162))
    right_ear_s.add_vertex((WIDTH - 235, 175))
    right_ear_s.add_vertex((WIDTH - 210, 186))
    right_ear_s.filled = True
    right_ear_s.fill_color = 'moccasin'
    right_ear_s.color = 'burlywood'

    # Ball on the face
    ball = GOval(80, 60, x=287, y=110)
    ball.filled = True
    ball.fill_color = 'white'
    ball.color = 'burlywood'

    # Ball left moccasin
    ball_lf = GPolygon()
    ball_lf.add_vertex((290, 130))
    ball_lf.add_vertex((315, 143))
    ball_lf.add_vertex((312, 158))
    ball_lf.add_vertex((307, 158))
    ball_lf.add_vertex((302, 158))
    ball_lf.add_vertex((297, 158))
    ball_lf.add_vertex((295, 157))
    ball_lf.add_vertex((293, 156))
    ball_lf.add_vertex((291, 153))
    ball_lf.add_vertex((289, 149))
    ball_lf.add_vertex((287, 145))
    ball_lf.add_vertex((287, 136))
    ball_lf.filled = True
    ball_lf.fill_color = 'moccasin'
    ball_lf.color = 'burlywood'

    # Ball right moccasin
    # ball_rf = GPolygon()
    ball_rf = GPolygon()
    ball_rf.add_vertex((WIDTH - 290, 130))
    ball_rf.add_vertex((WIDTH - 315, 143))
    ball_rf.add_vertex((WIDTH - 312, 158))
    ball_rf.add_vertex((WIDTH - 307, 158))
    ball_rf.add_vertex((WIDTH - 302, 158))
    ball_rf.add_vertex((WIDTH - 297, 158))
    ball_rf.add_vertex((WIDTH - 295, 157))
    ball_rf.add_vertex((WIDTH - 293, 156))
    ball_rf.add_vertex((WIDTH - 291, 153))
    ball_rf.add_vertex((WIDTH - 289, 149))
    ball_rf.add_vertex((WIDTH - 287, 145))
    ball_rf.add_vertex((WIDTH - 287, 136))
    ball_rf.filled = True
    ball_rf.fill_color = 'moccasin'
    ball_rf.color = 'burlywood'

    text = GLabel("I can code Python by learning stanCode")
    text.font = '-30'
    text.color = 'sienna'

    window.add(left_hand)
    window.add(left_hand_c)
    window.add(right_hand)
    window.add(right_hand_c)
    window.add(ball)
    window.add(ball_lf)
    window.add(ball_rf)
    window.add(face)
    window.add(face_lower_left)
    window.add(face_lower_right)
    window.add(small_face)
    window.add(nose)
    window.add(bv)
    window.add(bf)
    window.add(br)
    window.add(ba)
    window.add(left_eye)
    window.add(right_eye)
    window.add(left_line1)
    window.add(left_line2)
    window.add(left_line3)
    window.add(right_line1)
    window.add(right_line2)
    window.add(right_line3)
    window.add(left_eyebrow_b)
    window.add(left_eyebrow_m)
    window.add(right_eyebrow_b)
    window.add(right_eyebrow_m)
    window.add(left_ear_b)
    window.add(left_ear_s)
    window.add(right_ear_b)
    window.add(right_ear_s)
    window.add(text, (window.width - text.width)/2, 620)





if __name__ == '__main__':
    main()
