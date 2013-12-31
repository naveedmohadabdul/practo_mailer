<!DOCTYPE html>
<html>
<body>
<h1 style="text-align:center">Mass mailer mails</h1>
<h2> Mails sent </h2>
%for mail in mailer.find():
<hr>
<h3>Date_time : {{mail.get('dat_time')}}</h3>
<h3 style="color:#0266C8;">Username : {{mail['uid']}}</h4></h3> <br>
<h3 style="color:#F2B50F;">MailedTo  : {{','.join(mail['to_UID'])}}</h4></h3><br>
<h3 style="color:#00933B;">Subject   :{{mail['sub']}}</h4></h3><br> 
<h3>Message:</h4>
<h4 style="color:#F90101;"><pre>{{mail['msg']}}</pre></h4>
</div>
%end
</table>
</body>
</html>

