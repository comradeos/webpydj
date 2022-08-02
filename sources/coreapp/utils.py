from coreapp.models import Languages, Categories

class DataMixin:
    def get_user_context(self, **kwargs): 
        context = kwargs
        cats = Categories.objects.all()
        context['cats'] = cats
        
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
            
        return context