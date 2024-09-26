from score import *

def init():
    global rects
    rects = []
    global deadScore,raskeScore,smittetScore,mundbindScore,vaccineScore,imunScore,scoreBox,dødeScoreBox,raskeScoreBox,smittetScoreBox,mundbindScoreBox,vaccineretScoreBox,immunScoreBox,dødeChanceScoreBox,smitteChanceScoreBox
    deadScore = 0

    raskeScore = 0

    smittetScore = 0

    mundbindScore = 0

    vaccineScore = 0

    imunScore = 0

    scoreBox = []

    raskeScoreBox = Score(10,10,"raske",raskeScore)
    smittetScoreBox = Score(10,50,"smittede",smittetScore)
    dødeScoreBox = Score(10,90,"døde",deadScore)
    mundbindScoreBox = Score(10,130,"mundbind",mundbindScore)
    vaccineretScoreBox = Score(10,170,"vaccinerede",vaccineScore)
    immunScoreBox = Score(10,210,"immune",imunScore)

    smitteChanceScoreBox = Score(10,250,"smitte chance",0)
    dødeChanceScoreBox = Score(10,290,"døds chance",0)

    scoreBox.append(raskeScoreBox)
    scoreBox.append(smittetScoreBox)
    scoreBox.append(dødeScoreBox)
    scoreBox.append(mundbindScoreBox)
    scoreBox.append(vaccineretScoreBox)
    scoreBox.append(immunScoreBox)

    scoreBox.append(dødeChanceScoreBox)
    scoreBox.append(smitteChanceScoreBox)