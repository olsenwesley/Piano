# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:50:39 2020

@author: OlsenW
"""
#Create a function that, when called,runs the code that builds the sheet music
def ChopinPrelude20():

#Use the following libraries to access required modules 
    import abjad
    import copy
    
#Initialize the piano score and create empty upper/lower measure lists    
    score = abjad.Score()
    piano_staff = abjad.StaffGroup([], lilypond_type = 'PianoStaff')
    upper_staff = abjad.Staff()
    lower_staff = abjad.Staff()
    piano_staff.append(upper_staff)
    piano_staff.append(lower_staff)
    score.append(piano_staff)
    
    upper_measures = []
    lower_measures = copy.deepcopy(upper_measures)
    
#Create tuples containing notes and chords for the upper and lower measures   
    
#upper_tuple_1: contains chords for first four upper measures except for the
#third beat in each measure
    upper_tuple1 = (r"<g c' ef' g'>4 <af c' ef' af'>4 <ef g c' ef'>4",
                    r"<ef af c' ef'>4 <f af df' f'>4 <c ef af c'>4",
                    r"<d f b d'>4 <e g bf c' e'>4 <g c' ef'>4",
                    r"<fs c' d'>4 <g b d' g'>4 <b d' g'>4")
#upper_tuple_repeat_1: bars 5-8 repeat themselves in bars 9-12, so only write
#these notes once
    upper_tuple_repeat1 = (r"<ef' g' ef''>4 <ef' af' ef''>4 <d' g' d''>4",
                           r"<c' g' c''>4 <c' d' fs' d''>4 <b d' g'>4",
                           r"<c' g' c''>4 <af c' af'>4 <g c' ef'>4",
                           r"<ef af c' ef'>4 <f af df' f'>4 <ef g c'>4")
#Concatenate upper_tuple_repeat1 twice to create the entire repeated section
#bars 5-12
    upper_tuple_repeat = upper_tuple_repeat1 + upper_tuple_repeat1
#Concatenate upper_tuple1 and upper_tuple_repeat to get just one tuple for
#entire upper measure
    upper_tuple = upper_tuple1 + upper_tuple_repeat
#lower_tuple_1: contains chords for first four lower measures
    lower_tuple1 = (r"<c c,>4 <f,, f,>4 <g,, g,>4 <c, g, c>4",
                    r"<af, af,,>4 <df, df,,>4 <ef, ef,,>4 <af, af,,>4",
                    r"<g, g,,>4 <c, c,,>4 <f, f,,>4 <c c,>4",
                    r"<d a, d,>4 <g, g,,>4 <d, d,,>4 <g, g,,>4")
#lower_tuple_repeat_1: bars 5-8 repeat themselves in bars 9-12, so only write
#these notes once
    lower_tuple_repeat1 = (r"<c c,>4 <c c'>4 <b b,>4 <bf bf,>4",
                           r"<a a,>4 <af af,>4 <g g,>4 <f f,>4",
                           r"<ef ef,>4 <f f,>4 <b, b,,>4 <c c,>4",
                           r"<af, af,,>4 <df, df,,>4 <g, g,,>4 <c, c,,>4")
#Concatenate lower_tuple_repeat1 twice to create the entire repeated section
#bars 5-12
    lower_tuple_repeat = lower_tuple_repeat1 + lower_tuple_repeat1
#Concatenate lower_tuple1 and lower_tuple_repeat to get just one tuple for
#entire lower measure
    lower_tuple = lower_tuple1 + lower_tuple_repeat
#The third beat in each upper measure contains two voices
#voice_1_tuple1: contains notes for upper voice for first four upper measures
    voice_1_tuple1 = (r"<ef' g'>8. <d' f'>16",
                      r"<c' ef'>8. <bf df'>16",
                      r"g'8. f'16",
                      r"b'8. a'16")
#voice_1_tuple_repeat1: bars 5-8 repeat themselves in bars 9-12, so only write
#these notes once for upper voice
    voice_1_tuple_repeat1 = (r"<d' d''>4",
                             r"<g' b'>8. a'16",
                             r"g'8. f'16",
                             r"ef'8. d'16")
#Concatenate voice_1_tuple_repeat1 twice to create the entire repeated section
#bars 5-12
    voice_1_tuple_repeat = voice_1_tuple_repeat1 + voice_1_tuple_repeat1
#Concatenate voice_1_tuple1 and voice_1_tuple_repeat to get just one tuple
#for entire upper measure third beat upper voice
    voice_1_tuple = voice_1_tuple1 + voice_1_tuple_repeat
#voice_2_tuple1: contains notes for lower voice for first four upper measures
    voice_2_tuple1 = (r"<g b>4",
                      r"<df ef g>4",
                      r"<af c'>4",
                      r"<c' d' fs'>4")
#voice_2_tuple_repeat1: bars 5-8 repeat themselves in bars 9-12, so only write
#these notes once for lower voice
    voice_2_tuple_repeat1 = (r"af'8. fs'16",
                             r"d'8. c'16",
                             r"<g d'>4",
                             r"<f g b>4")
#Concatenate voice_2_tuple_repeat1 twice to create the entire repeated section
#bars 5-12
    voice_2_tuple_repeat = voice_2_tuple_repeat1 + voice_2_tuple_repeat1
#Concatenate voice_2_tuple1 and voice_2_tuple_repeat to get just one tuple
#for entire upper measure third beat lower voice
    voice_2_tuple = voice_2_tuple1 + voice_2_tuple_repeat
    
#Executing this while loop appends upper and lower measures at each iteration
#These measures are popuplated with the tuples defined above
#The upper and lower voices are treated separately; container created for
#third beat, then container inserted into correct position in upper measures
    i = 0
    while i <= 11:
        upper_measures.append(abjad.Measure((4,4), []))
        lower_measures.append(abjad.Measure((4,4), []))
        
        upper_measures[i].extend(upper_tuple[i])
        lower_measures[i].extend(lower_tuple[i])
        
        voice_1 = abjad.Voice(voice_1_tuple[i])
        voice_2 = abjad.Voice(voice_2_tuple[i])
        literal_1 = abjad.LilyPondLiteral(r"\voiceOne")
        literal_2 = abjad.LilyPondLiteral(r"\voiceTwo")
        abjad.attach(literal_1, voice_1[0])
        abjad.attach(literal_2, voice_2[0])
        container = abjad.Container([voice_1, voice_2], is_simultaneous = True)
        upper_measures[i].insert(2, container)
        
        i += 1
    
#Create final empty measure for final chord
    upper_measures.append(abjad.Measure((4,4), []))
    lower_measures.append(abjad.Measure((4,4), []))
#Append the chords to the final measures
    upper_measures[12].append(r"<c' ef' g' c''>1")
    lower_measures[12].append("<c g>1")
#Extend the intial piano staff to include the measures created above
    upper_staff.extend(upper_measures)
    lower_staff.extend(lower_measures)
    
#Set and place clefs throughput piece
    leaf1 = abjad.inspect(lower_staff).leaf(0)
    leaf2 = abjad.inspect(upper_staff).leaf(0)
    leaf3 = abjad.inspect(upper_staff).leaf(20)
    leaf4 = abjad.inspect(upper_staff).leaf(43)
    leaf5 = abjad.inspect(upper_staff).leaf(49)
    leaf6 = abjad.inspect(upper_staff).leaf(68)
    leaf7 = abjad.inspect(upper_staff).leaf(74)
    abjad.attach(abjad.Clef('bass'), leaf1)
    abjad.attach(abjad.Clef('bass'), leaf2)
    abjad.attach(abjad.Clef('treble'), leaf3)
    abjad.attach(abjad.Clef('bass'), leaf4)
    abjad.attach(abjad.Clef('treble'), leaf5)
    abjad.attach(abjad.Clef('bass'), leaf6)
    abjad.attach(abjad.Clef('treble'), leaf7)
    
#Set key signature for left and right hand
    key_signature = abjad.KeySignature('c', 'minor')
    abjad.attach(key_signature, leaf1)
    key_signature2 = abjad.KeySignature('c', 'minor')
    abjad.attach(key_signature2, leaf2)
    
#Attach necessary dynamics to piece and insert in correct positions
    abjad.attach(abjad.Dynamic('ff'), upper_measures[0][0])
    abjad.attach(abjad.Dynamic('p'), upper_measures[4][0])
    abjad.attach(abjad.Dynamic('pp'), upper_measures[8][0])
    abjad.attach(abjad.Dynamic('p'), upper_measures[12][0])

#Add bar line after measure 12
    bar_line = score.add_final_bar_line()
    
#Add tempo and other markups to piece at required positions
    markup = abjad.Markup('Largo', direction = abjad.Up).italic()
    abjad.attach(markup, upper_measures[0][0])
    
    markup2 = abjad.Markup('riten.', direction = abjad.Up).italic()
    abjad.attach(markup2, upper_measures[6][3])
    
    markup3 = abjad.Markup('cresc.', direction = abjad.Down).italic()
    abjad.attach(markup3, upper_measures[9][1])
    
#Add fermata to last chord of piece
    fermata = abjad.Fermata()
    abjad.attach(fermata, upper_measures[12][0])
    abjad.attach(fermata, lower_measures[12][0])
    
#Add accent to last chord of piece
    accent = abjad.Articulation('accent')
    abjad.attach(accent, upper_measures[12][0])
    
#initialize the final lilypond file for formatting
    lilypond_file = abjad.LilyPondFile.new(music = score, global_staff_size = 20,
                                              default_paper_size = ('A5', 'portait'),)
    
#Add title, composer, etc. to the sheet
    lilypond_file.header_block.title = abjad.Markup('Prelude')
    lilypond_file.header_block.composer = abjad.Markup('Frederic Chopin')
    lilypond_file.header_block.tagline = abjad.Markup('Written in Python using the Abjad library and Lilypond engraving software - Wesley Olsen')
    lilypond_file.header_block.subsubtitle = abjad.Markup('Op. 20 No. 28')
    
#Create Lilypond file and .pdf
    abjad.show(lilypond_file)