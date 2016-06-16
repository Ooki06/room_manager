import sqlite3

def addData(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'room_manager/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
    	conn = sqlite3.connect("db.sqlite3")
		conn.execute("insert into order values( '1', '1', '1', '1', '1/1', '0', '0'  )")
		conn.execute("insert into order values( '1', '1', '1', '1', '1/1', '0', '0'  )")
