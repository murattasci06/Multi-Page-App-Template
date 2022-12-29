import streamlit as st
import streamlit.components.v1 as components

# Customization for heading
st.title("Get in Touch with Us !")

st.markdown('<style>div[class="css-zt5igj e16nr0p33"] {color:white; text-align:center;font-size:50px; font-family: Lucida Handwriting; margin-bottom:0.001px;  } </style>', unsafe_allow_html=True)


# Customization for image
st.markdown('<img src="https://images.assetsdelivery.com/compings_v2/rondale/rondale1608/rondale160800047.jpg" alt width="1366" height="250" style="transform:rotate(0deg); filter: blur(3px);"/>', unsafe_allow_html=True)


st.markdown('<style>div[class="css-1offfwp e16nr0p34"] {margin-top:-20px;  } </style>', unsafe_allow_html=True)


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
    
    
#menu color
st.markdown('<style>div[class="css-14xtw13 e8zbici0"] { color:white;} </style>', unsafe_allow_html=True)


# Hiding the decoration
st.markdown('<style>div[class="css-1dp5vir e8zbici1"] { display:none;} </style>', unsafe_allow_html=True)


#contact
components.html("""<html>


<head>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" />


</head>

<body>
    <div class="icons">
		
		
		<a href="https://www.linkedin.com/">
		   <div class="layer">
		   <span></span>
		   <span></span>
		   <span></span>
		   <span></span>
		   <span class="fab fa-linkedin-in"</span>
		
	   
		   </div>
		   <div class="text">Linkedin</div>
		</a>
		
		<a href="https://accounts.google.com">
		   <div class="layer">
		   <span></span>
		   <span></span>
		   <span></span>
		   <span></span>
		   <span class="fab fa-google-plus-g"</span>
		
	   
		   </div>
		   <div class="text">Google</div>
		</a>
		
		<a href="https://twitter.com/">
		   <div class="layer">
		   <span></span>
		   <span></span>
		   <span></span>
		   <span></span>
		   <span class="fab fa-twitter"</span>
		
	   
		   </div>
		   <div class="text">Twitter</div>
		</a>
		
		

		<a href="https://github.com/">
			   <div class="layer">
			   <span></span>
			   <span></span>
			   <span></span>
			   <span></span>
			   <span class="fab fa-github"</span>

		   
			   </div>
			   <div class="text">GitHub</div>
		</a>

    </div>

    

</body>

<style>


*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;


}


html,body{
display:grid;
height:100%;
place-items:center;
background:#000;

}

.icons{
display:inline-flex;
}

.icons a{
margin:0 25px;
text-decoration:none;
color:#fff;
display:block;
position:relative;
bottom:14px;
}


.icons a .layer{
width:90px;
height: 90px;
transition:transform 0.3s;

}

.icons a:hover .layer{
transform:rotate(-35deg) skew(20deg);

}


.icons a .layer span{
position:absolute;
top: 0;
left: 0;

height:100%;
width:100%;
border: 1px solid #fff;
border-radius: 5px;
transition:all 0.3s;
}


.icons a .layer span.fab{
font-size:30px;
line-height:80px;
text-align:center;

}


.icons a .text{
position:absolute;
left:50%;
bottom:-5px;
opacity:0;
transform:translateX(-50%);
transition:bottom 0.3s ease, opacity 0.3s ease;
}


.icons a:hover .text{
opacity:1;
bottom:-35px;
}

.icons a:hover .layer span:nth-child(1){
opacity:0.2;
}

.icons a:hover .layer span:nth-child(2){
opacity:0.4;
transform:translate(5px, -5px);
}

.icons a:hover .layer span:nth-child(3){
opacity:0.6;
transform:translate(10px, -10px);
}

.icons a:hover .layer span:nth-child(4){
opacity:0.8;
transform:translate(15px, -15px);
}

.icons a:hover .layer span:nth-child(5){
opacity:1;
transform:translate(20px, -20px);
}

.icons a:nth-child(1) .layer span,
.icons a:nth-child(1) .text{
color:#CACCCE;
border-color:#CACCCE
}

.icons a:nth-child(2) .layer span,
.icons a:nth-child(2) .text{
color:#DB4A39;
border-color:#DB4A39;
}

.icons a:nth-child(3) .layer span,
.icons a:nth-child(3) .text{
color:#1DA1F2;
border-color:#1DA1F2;
}

.icons a:nth-child(4) .layer span,
.icons a:nth-child(4) .text{
color:##2867B2;
border-color:##2867B2;
}

.icons a:nth-child(1) .layer span{
box-shadow:-1px 1px 3px #CACCCE;
}

.icons a:nth-child(2) .layer span{
box-shadow:-1px 1px 3px #DB4A39;
}
.icons a:nth-child(3) .layer span{
box-shadow:-1px 1px 3px #1DA1F2;
}

.icons a:nth-child(4) .layer span{
box-shadow:-1px 1px 3px ##2867B2;
}

</style>

   
</html>""",height=352)


#header
css = '''

.stApp > header {
    background-color: black;
    opacity: 0;
}

'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
#inline of contact container 
st.markdown('<style>div[class="appview-container css-1wrcr25 egzxvld4"] {background-color:black; background-size: cover;} </style>', unsafe_allow_html=True)