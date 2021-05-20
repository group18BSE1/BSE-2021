# progrom extracts characters after the colon and prints a floating number
st = "X-DSPAM-Confidence:0.8475"
extr = st.find(":")
num = st[extr + 1:]
print(float(num))
