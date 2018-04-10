book_result_stylesheet="""
QLabel {

    font-size:25px;
    color:#0a0505;
    background: #f0f9f0;
}


"""

signup_stylesheet="""
QLabel {

    font-size:20px;
    color:#0a0505;
    background: #f0f9f0;
}

QLineEdit {
    border: 2px solid gray;
    border-radius: 10px;
    height:25px;
    width:300px;
    font-size:15px;
    color:#0a0505;
    padding: 0 8px;
    background: #f0f9f0;
    selection-background-color: darkgray;
}

QPushButton {

	box-shadow: 0px 10px 14px -7px #276873;
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #599bb3, stop: 1 #408c99);
	background-color:#599bb3;
	border-radius:8px;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	padding:5px 20px;
	font-weight:bold;
	text-decoration:none;
	text-shadow:0px 1px 0px #3d768a;
}

QPushButton:hover {
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #408c99, stop: 1 #599bb3);
	background-color:#408c99;
}

QPushButton:pressed {
	top:1px;
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #346e78, stop: 1 #22565f);
}

"""