'''Difference between available fonts in Ubuntu 22 vs Windows 10 (Ubuntu install has had microsoft fonts installed)'''

# Author: Luke Henderson

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt
import logger as lg

cl.green('Program Start')
progStart = time.time()



linuxFonts = ('Standard Symbols PS', 'Lohit Kannada', 'Samyak Devanagari', 'Sree Krushnadevaraya', 'URW Gothic', 'OpenSymbol', 'Khmer OS System', 'Nakula', 'Chandas', 'Potti Sreeramulu', 'Andale Mono', 'Keraleeyam', 'Trebuchet MS', 'Meera', 'Nimbus Roman', 'Gurajada', 'Webdings', 'Kalimati', 'Peddana', 'KacstQurn', 'Gubbi', 'Tibetan Machine Uni', 'Umpush', 'DejaVu Sans Mono', 'Arial Black', 'Purisa', 'Pothana2000', 'Noto Serif CJK JP', 'KacstBook', 'KacstLetter', 'Noto Serif CJK KR', 'Noto Serif CJK HK', 'Norasi', 'Loma', 'Karumbi', 'Verdana', 'KacstDigital', 'KacstTitleL', 'mry_KacstQurn', 'Noto Serif CJK SC', 'Noto Serif CJK TC', 'Likhan', 'RaghuMalayalamSans', 'Mallanna', 'Yrsa', 'Padauk Book', 'Phetsarath OT', 'Sawasdee', 'Sahadeva', 'Rasa', 'Nimbus Sans', 'NATS', 'Tlwg Typist', 'Noto Sans Mono CJK SC', 'Tlwg Typewriter', 'Noto Sans Mono CJK TC', 'Manjari', 'Ubuntu', 'Noto Sans Mono CJK JP', 'Samyak Tamil', 'Noto Sans Mono CJK HK', 'Noto Sans Mono CJK KR', 'Yrsa', 'Ubuntu', 'Chilanka', 'FreeSerif', 'Times New Roman', 'Dhurjati', 'Nimbus Mono PS', 'Lohit Assamese', 'Padauk', 'AnjaliOldLipi', 'Ubuntu Condensed', 'Samyak Gujarati', 'Rasa', 'ori1Uni', 'KacstOffice', 'Nimbus Sans Narrow', 'URW Bookman', 'Ramabhadra', 'DejaVu Sans', 'Kinnari', 'LakkiReddy', 'KacstArt', 'Lohit Odia', 'Tlwg Mono', 'Ponnala', 'Noto Sans Mono', 'aakar', 'Bitstream Charter', 'KacstOne', 'Ramaraja', 'Kalapi', 'Comic Sans MS', 'NTR', 'Khmer OS', 'Courier 10 Pitch', 'C059', 'Laksaman', 'Liberation Sans Narrow', 'Liberation Mono', 'padmaa-Bold.1.1', 'Manjari', 'Timmana', 'Mukti', 'Mandali', 'Rachana', 'Pagul', 'Lohit Telugu', 'Lohit Tamil Classical', 'Gayathri', 'Samanata', 'Droid Sans Fallback', 'RaviPrakash', 'Z003', 'Vemana2000', 'Gidugu', 'Lohit Gujarati', 'KacstPen', 'D050000L', 'KacstDecorative', 'TenaliRamakrishna', 'Suranna', 'Liberation Serif', 'Syamala Ramana', 'Lohit Malayalam', 'LKLUG', 'Ubuntu', 'Noto Sans CJK HK', 'Noto Sans CJK KR', 'KacstPoster', 'Noto Sans CJK JP', 'Liberation Sans', 'Noto Sans CJK SC', 'Ani', 'Rasa', 'Noto Sans CJK TC', 'FreeSans', 'Sarai', 'Yrsa', 'Georgia', 'Lohit Devanagari', 'Noto Color Emoji', 'Uroob', 'Noto Mono', 'KacstNaskh', 'Dyuthi', 'Lohit Tamil', 'Tlwg Typo', 'KacstFarsi', 'Suruma', 'Lohit Bengali', 'Arial', 'Abyssinica SIL', 'Jamrul', 'Mitra', 'Courier New', 'Waree', 'KacstTitle', 'P052', 'padmaa', 'DejaVu Serif', 'Saab', 'Yrsa', 'Navilu', 'Gargi', 'Garuda', 'Samyak Malayalam', 'Rekha', 'KacstScreen', 'Impact', 'Lohit Gurmukhi', 'FreeMono', 'Ubuntu Mono', 'Suravaram', 'Gayathri', 'Rasa')