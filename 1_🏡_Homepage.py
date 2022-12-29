import streamlit as st

import streamlit.components.v1 as components


# Page config
st.set_page_config(
        page_title= "Multipage App",
        page_icon="🔲")



# Customization for sidebar
st.markdown('<style>div[class="css-6qob1r e1fqkh3o3"] { background: url("https://thumbs.gfycat.com/FirmAchingBillygoat-size_restricted.gif");background-repeat: no-repeat;background-size:600%; border-right: 1px solid #FFFAFA;  border-image: linear-gradient( #D3D3D3, black) 0.75;  margin-top:-2px;} </style>', unsafe_allow_html=True)

# Customization for crossed out
st.markdown('<style>div[class="css-1xtoq5p e1fqkh3o2"] {color:white;  } </style>', unsafe_allow_html=True)

# Customization for collapsedControl
st.markdown('<style>div[class="css-y4qlto e1fqkh3o1"] {color:white;  } </style>', unsafe_allow_html=True)


# Hiding the Footer
hide_st_style =" <style>footer {visibility: hidden;}</style>"
st.markdown(hide_st_style, unsafe_allow_html=True)  


#side bar customization
st.markdown("""
  <style>
      ul[class="css-uc76bn e1fqkh3o9"]{
        position: relative;
        position: relative;
        padding-top: 3rem;
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: left;
  
      }
      
      
      .css-17lntkn {
        font-weight: bold;
        font-size: 24px;
        color: white;
        text-shadow: -1.5px 0 black, 0 1.5px black, 2px 0 black, 0 -1.5px black;
        font-family: arial;
        border:black;
      }
      
      .css-pkbazv {
        font-weight: bold;
        font-size: 24px;
        color: white;
        text-shadow: -1.5px 0 black, 0 1.5px black, 1.5px 0 black, 0 -1.5px black;
        font-family: arial;
      }
  </style>""", unsafe_allow_html=True)

# margin between emoji and text
st.markdown("""
    <style>
    .css-8hkptd {
            margin-right: 4.5px;
        }
    </style>""", unsafe_allow_html=True)


#homepage animation
components.html("""<html><body>

<section>
       
<h1>
<span>W</span>
<span>E</span>
<span>L</span>
<span>C</span>
<span>O</span>
<span>M</span>
<span>E</span>
</h1> 
</section>


<style>


body {
  margin: 0;
  padding: 0;
  background: black;


}

section {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  position: relative;
}

section::before {

  position: absolute;
  content: '';
  inset: 0;
  background: url('https://c4.wallpaperflare.com/wallpaper/445/682/456/5bd20f8a67dd1-wallpaper-preview.jpg');
  background-size: cover;
  background-position: center;
  opacity: 0;
  
  animation: fadeInBackground 1s linear 8.5s forwards;
}

h1 {
  margin: 0px;
  padding: 0px;
  color: #ddd;
  font-size: min(9vw, 9rem);
  font-family: sans-serif;

}

h1 span {
   display: inline-block;
   animation: letterAnimation 1s linear forwards;
   border:2px solid black;
   border-radius: 4px;
   padding: 0.25rem;
   padding-bottom: 0;

  
}

@keyframes fadeInBackground {
  100% {
    opacity: 1;
  }
}

@keyframes letterAnimation {
  100% {
    opacity: 1;
	color: red;
	padding: 0.25rem;
	padding-bottom: 0;
	background-color: white;
    border: 2px solid red;
	border-radius: 4px;
	text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
	box-sizing: border-box;
  }
}

h1 span:nth-child(1) {
  animation-delay: 1.5s;
}

h1 span:nth-child(2) {
  animation-delay: 2.5s;
}

h1 span:nth-child(3) {
  animation-delay: 3.5s;
}

h1 span:nth-child(4) {
  animation-delay: 4.5s;
}

h1 span:nth-child(5) {
  animation-delay: 5.5s;
}

h1 span:nth-child(6) {
  animation-delay: 6.5s;
}

h1 span:nth-child(7) {
  animation-delay: 7.5s;
}



    
</style>

</body>
</html>""")

#inline of welcome container 
st.markdown('<style>div[class="appview-container css-1wrcr25 egzxvld4"] {background-color:black; background-size: cover;} </style>', unsafe_allow_html=True)

#header
css = '''

.stApp > header {
    background-color: black;
}

'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



#menu color
st.markdown('<style>div[class="css-14xtw13 e8zbici0"] { color:white;} </style>', unsafe_allow_html=True)


# Hiding the decoration
st.markdown('<style>div[class="css-1dp5vir e8zbici1"] { display:none;} </style>', unsafe_allow_html=True)