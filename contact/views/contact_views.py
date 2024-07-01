from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from contact.models import Contact

def search(request):
    search_value = request.GET.get('q','').strip()
    if search_value == '':
        return redirect("contact:index")
    
    contacts = Contact.objects.filter(show=True).filter(Q(frist_name__icontains=search_value)|
                                                        (Q(last__icontains=search_value))).order_by('-id')
    print(contacts.query)
    
    

    print(search_value)

    context = {
        'contacts': contacts,
        'site_title':'Contatos - ' 
    }

    return render(
        request,'contact/index.html',context
    )


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")[:10]\
    
    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title':'Contatos - ' 
    }

    return render(
        request,'contact/index.html',context
    )

def contact(request,contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact.objects,pk=contact_id,show=True)
    
    contact_name = f'{single_contact.frist_name} {single_contact.last} - '

    context = {
        'contact': single_contact,
        'site_title':contact_name,

    }

    return render(
        request,'contact/contact.html',context
    )