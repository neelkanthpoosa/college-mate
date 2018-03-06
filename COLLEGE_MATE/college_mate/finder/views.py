from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from finder.forms import FinderForm
from finder.models import Post

class FinderView(TemplateView):
	template_name='finder/finder.html'


	def get(self,request):
		form=FinderForm()
		posts=Post.objects.all().order_by('-created')
		#print(posts)
		args={'form':form,'posts':posts}
		return render(request,self.template_name,args)


	def post(self,request):
		form =  FinderForm(request.Post)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']

			image=form.cleaned_data['post']
			form=FinderForm()
			return redirect('finder:finder')
		args={'form':form,'text':text,'image':image}
		return render(request,self.template_name,args)
		# form = FinderForm(request.POST)
		# if request.method=='POST':
			# form = FinderForm(request.POST)
	        #
			# if form.is_valid():
			# 	post=form.save(commit=False)
			# 	post.user=request.user
			# 	post.save()
			# 	text=form.cleaned_data['post']
	        #
			# 	form=FinderForm()
			# 	return redirect('finder:finder')
	        #
			# else:
			# 	form=FinderForm(instance=request.user)
			# 	return redirect('finder:finder')
