from flask import Flask
from flask import request
from twilio.rest import TwilioRestClient 
import random
	
def printBoard(board):
	print board[0],"|",board[1],"|",board[2]
	print "----------"
	print board[3],"|",board[4],"|",board[5]
	print "----------" 
	print board[6],"|",board[7],"|",board[8]
	print

def makeMove(board, player):
	winningMove = findWin(board, player)
	print winningMove
	if(checkBoard(board)!=None):
		return None
	else:
		if ((winningMove!=(None, None)) and (board[winningMove[1]]==" ")):
			if (winningMove[0]==player):
				board[winningMove[1]] = player
				# player has won
				return player
			else:
				board[winningMove[1]] = player	
		elif(board[4]==" "):
			board[4]=player
		elif(findCorner(board, player)!=None):
			board[findCorner(board, player)] = player
		else:
			index = getRandomOpenSpot(board)
			board[index] = player

	return board

def getRandomOpenSpot(board):
	openSpots = []
	for spot in xrange(0,len(board)):
		if board[spot]==" ":
			openSpots.append(spot)
	return random.choice(openSpots)
	
def findCorner(board,player):
	#will find an opposite of a opponents corner

	if ((board[0]!=" ") and (board[0]!=player) and (board[8]==" ")):
		return 8
	elif ((board[2]!=" ") and (board[0]!=player) and (board[6]==" ")):
		return 6
	elif ((board[6]!=" ") and (board[0]!=player) and (board[2]==" ")):
		return 2
	elif ((board[8]!=" ") and (board[0]!=player) and (board[0]==" ")):
		return 0
	else:
		return None	

def findWin(board, player):
	#return (winningPlayer, winningSpot)
	winningSpot = None
	winningPlayer = None

	if ((board[0] == board[1] != " ") and board[2] == " "):
		winningSpot = 2
		winningPlayer = board[0]
	elif ((board[0] == board[4] != " ") and board[8] == " "):
		winningSpot = 8
		winningPlayer = board[0]
	elif ((board[0] == board[3] != " ") and board[6] == " "):
		winningSpot = 6
		winningPlayer = board[0]
	elif ((board[0] == board[2] != " ") and board[1] == " "):
		winningSpot = 1
		winningPlayer = board[0]
	elif ((board[0] == board[8] != " ") and board[4] == " "):
		winningSpot = 4
		winningPlayer = board[0]
	elif ((board[0] == board[6] != " ") and board[3] == " "):
		winningSpot = 3
		winningPlayer = board[0]
	
	elif ((board[1] == board[2] != " ") and board[3] == " "):
		winningSpot = 3
		winningPlayer = board[1]
	elif ((board[1] == board[4] != " ") and board[7] == " "):
		winningSpot = 7
		winningPlayer = board[1]
	elif ((board[1] == board[7] != " ") and board[4] == " "):
		winningSpot = 4
		winningPlayer = board[1]

	elif ((board[2] == board[4] != " ") and board[6] == " "):
		winningSpot = 6
		winningPlayer = board[2]
	elif ((board[2] == board[5] != " ") and board[8] == " "):
		winningSpot = 8
		winningPlayer = board[2]
	elif ((board[2] == board[6] != " ") and board[4] == " "):
		winningSpot = 4
		winningPlayer = board[2]
	elif ((board[2] == board[8] != " ") and board[5] == " "):
		winningSpot = 5
		winningPlayer = board[2]

	elif ((board[3] == board[4] != " ") and board[5] == " "):
		winningSpot = 5
		winningPlayer = board[3]
	elif ((board[3] == board[6] != " ") and board[0] == " "):
		winningSpot = 0
		winningPlayer = board[3]
	elif ((board[3] == board[5] != " ") and board[4] == " "):
		winningSpot = 4
		winningPlayer = board[3]

	elif ((board[4] == board[6] != " ") and board[2] == " "):
		winningSpot = 2
		winningPlayer = board[4]
	elif ((board[4] == board[7] != " ") and board[1] == " "):
		winningSpot = 1
		winningPlayer = board[4]
	elif ((board[4] == board[8] != " ") and board[0] == " "):
		winningSpot = 0
		winningPlayer = board[4]

	elif ((board[5] == board[8] != " ") and board[2] == " "):
		winningSpot = 2
		winningPlayer = board[5]
	elif ((board[5] == board[4] != " ") and board[3] == " "):
		winningSpot = 3
		winningPlayer = board[6]

	elif ((board[6] == board[7] != " ") and board[8] == " "):
		winningSpot = 8
		winningPlayer = board[5]
	elif ((board[6] == board[8] != " ") and board[7] == " "):
		winningSpot = 7
		winningPlayer = board[6]

	elif ((board[7] == board[8] != " ") and board[6] == " "):
		winningSpot = 6
		winningPlayer = board[7]

	return (winningPlayer, winningSpot)


def checkBoard(board):
	if (" " not in board):
		return " "
	elif(board[0]==board[1]==board[2]!=" "):
		return board[0]
	elif(board[3]==board[4]==board[5]!=" "):
		return board[3]
	elif(board[6]==board[7]==board[8]!=" "):
		return board[6]
	elif(board[0]==board[3]==board[6]!=" "):
		return board[0]
	elif(board[1]==board[4]==board[7]!=" "):
		return board[1]
	elif(board[2]==board[5]==board[8]!=" "):
		return board[2]
	elif(board[0]==board[4]==board[8]!=" "):
		return board[0]
	elif(board[2]==board[4]==board[6]!=" "):
		return board[2]
	else:
		return None

def parseBoardIn(input):
	board=range(9)
	count=0
	for index in xrange(0,len(input)):
		print input[index]
		if(input[index]=="_"):
			board[count]=" "
			count+=1
		elif(input[index].lower()=="x" or input[index].lower()=="o"):
			board[count]=(input[index].lower())
			count+=1
	return board

def parseBoardOut(input):
	for x in xrange(0,len(input)):
		if(input[x]==" "):
			input[x]="_"
	boardStr = "%s|%s|%s\n%s|%s|%s\n%s|%s|%s" % (input[0], input[1], input[2], input[3], input[4], input[5], input[6], input[7], input[8])
	return boardStr


# put your own credentials here 
ACCOUNT_SID = "<ACCOUNT_SID>" 
AUTH_TOKEN = "<AUTH_TOKEN>" 
PHONE_NUM = "<TWILIO NUMBER>"


 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

app = Flask(__name__)

@app.route('/', methods=['POST'])
def recieveText():
	print request.form['From']
	body=request.form['Body']
	fromNum = request.form['From']
	print type(request.form['Body'])
	board= "_|_|_\n_|_|_\n_|_|_"

	if(str(body)=="New game"):
		client.messages.create(
		    to=fromNum,
			from_=PHONE_NUM,
		    body="You are playing as x", 
		)
		responseText=board
	else:
		board = parseBoardIn(str(request.form['Body']))
		
		# debug:
		# print "--------incoming---------"
		# printBoard(board)
		# print "-------------------------"

		board = makeMove(board,'o')
		if (board==None):
			responseText = "The game is over, please start a new game"
		elif(board=="x" or board=="o"):
			responseText = board,"has won"
		else:
			responseText = parseBoardOut(board)
		
		# debug:
		# print "--------outgoing---------"
		# printBoard(board)
		# print responseText
		# print "-------------------------"

	client.messages.create(
	    to=fromNum,
		from_=PHONE_NUM,
	    body=responseText, 
	)
	return "message recieved"


if __name__ == '__main__':
	app.run(debug=True)