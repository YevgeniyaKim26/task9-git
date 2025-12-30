{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def process_numbers():\
    n = 0\
    s = 0\
    m = None\
\
    while True:\
        x = int(input("Enter number: "))\
\
        if x == -1:\
            break\
\
        if n == 0:\
            m = x\
        elif x < m:\
            m = x\
\
        s = s + x\
        n = n + 1\
\
    if n == 0:\
        m = -1\
        a = -1\
    else:\
        a = s / n\
\
    print("n =", n)\
    print("s =", s)\
    print("m =", m)\
    print("a =", a)\
\
\
process_numbers()}