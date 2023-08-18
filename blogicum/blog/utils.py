from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Comment


class PostMixin():
    def filtered_post(self, post_list):
        return post_list.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )


class CommentMixin(LoginRequiredMixin):
    model = Comment
    template_name = 'blog/comment.html'
    pk_url_kwarg = ('comment_id')

    def dispatch(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs['comment_id'])
        if comment.author != self.request.user:
            return redirect(
                'blog:post_detail',
                pk=self.kwargs['pk']
            )
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.kwargs["pk"]})
