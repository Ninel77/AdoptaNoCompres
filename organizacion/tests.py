'''
class ActualizardatosBAnimN(UpdateView):
    model = AnimalesDatosB
    template_name = 'animales/ActSoloDatosAnimales.html'
    form_class = DatoBasicosAnimales
    success_url = reverse_lazy('animal:ListaAnimTodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Basicos del Animal de Compañia '
        context['entity'] = 'Actualizar Datos Basicos'
        context['accion'] = 'Actualizar'
        context['accion2'] = 'Cancelar'
        return context


class ActualizarDatosEval(UpdateView):
    model_apoyo = AnimalesDatosB
    model = InfoEvaluacion
    template_name = 'animales/ActSoloDatosAnimales.html'
    form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimTodo')

    def get_context_data(self, **kwargs):
        context = super(ActualizarDatosEval, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Evaluacion'
        context['accion'] = 'Actualizar'
        pk = self.kwargs.get('pk', 0)
        DatosAnim = self.model_apoyo.objects.get(id=pk)
        Eval = self.model.objects.get(id=DatosAnim.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_DatosAnim = kwargs['pk']
        DatosAnim = self.model_apoyo.objects.get(id=id_DatosAnim)
        Eval = self.model.objects.get(id=DatosAnim.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=Eval)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ActualizarAnimEnAdop(UpdateView):
    model = AnimalesEnAdopcion
    model_segundo = AnimalesDatosB
    model_tercero = InfoEvaluacion
    template_name = 'animales/ActAnimEnAdop.html'
    form_class = AnimEnAdopcion
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimEnAdop')

    def get_context_data(self, **kwargs):
        context = super(ActualizarAnimEnAdop, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Animal en adopcion'
        context['tituloPrim'] = 'Actualizar Datos Animal en adopcion'
        context['tituloSec'] = 'Actualizar Datos Basicos'
        context['tituloTer'] = 'Actualizar Datos Evaluacion'
        context['accion'] = 'Actualizar'
        pk = self.kwargs.get('pk', 0)
        EnAdop = self.model.objects.get(id=pk)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=DatosAnim)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=EvalMed)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalEnAdopcion = kwargs['pk']
        EnAdop = self.model.objects.get(id=id_AnimalEnAdopcion)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=EnAdop)
        form2 = self.segundo_form_class(request.POST, instance=DatosAnim)
        form3 = self.tercer_form_class(request.POST, instance=EvalMed)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form3.save()
            form2.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class ActualizarAnimResc(UpdateView):
    model = AnimalesRescatados
    model_segundo = AnimalesDatosB
    model_tercero = InfoEvaluacion
    template_name = 'animales/ActAnimResc.html'
    form_class = AnimRescatados
    segundo_form_class = DatoBasicosAnimales
    tercer_form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimEnRehab')

    def get_context_data(self, **kwargs):
        context = super(ActualizarAnimResc, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Animal en adopcion'
        context['accion'] = 'Actualizar'
        context['tituloPrim'] = 'Actualizar Datos de Rescate'
        context['tituloSec'] = 'Actualizar Datos de Animal'
        context['tituloTer'] = 'Actualizar Datos de Evaluacion'

        pk = self.kwargs.get('pk', 0)
        EnAdop = self.model.objects.get(id=pk)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.segundo_form_class(instance=DatosAnim)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=EvalMed)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalEnAdopcion = kwargs['pk']
        EnAdop = self.model.objects.get(id=id_AnimalEnAdopcion)
        DatosAnim = self.model_segundo.objects.get(id=EnAdop.animal_id)
        EvalMed = self.model_tercero.objects.get(id=EnAdop.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=EnAdop)
        form2 = self.segundo_form_class(request.POST, instance=DatosAnim)
        form3 = self.tercer_form_class(request.POST, instance=EvalMed)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            form3.save()
            form2.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class ActualizarRegAdopcion(UpdateView):
    model = AnimalesAdoptados
    model_segundo = DocumentosAdopcion
    model_tercero = AnimalesDatosB
    model_cuarto = Adoptante
    model_quinto = DatosPersonales
    model_sexto = InfoEvaluacion
    template_name = 'animales/RegistroAdopcion.html'
    form_class = AnimalesAdop
    segundo_form_class = DocAdopcion
    tercer_form_class = DatoBasicosAnimales
    cuarto_form_class = DatosAdoptante
    quinto_form_class = RegPersona
    sexto_form_class = DatosMedicos
    success_url = reverse_lazy('animal:ListaAnimAdop')

    def get_context_data(self, **kwargs):
        context = super(ActualizarRegAdopcion, self).get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Datos Animal Adoptado'
        context['accion'] = 'Actualizar'
        context['tituloPrim'] = 'Registrar Datos para la Adopcion'
        context['tituloSec'] = 'Actualizar datos del animal'
        context['tituloTer'] = 'Registrar datos adoptante'

        pk = self.kwargs.get('pk', 0)
        Adop = self.model.objects.get(id=pk)
        DocAdop = self.model_segundo.objects.get(id=Adop.documentos_id)
        DatosAnim = self.model_tercero.objects.get(id=Adop.animal_id)
        DatosAdop = self.model_cuarto.objects.get(id=Adop.adoptante_id)
        DatosPersonaA = self.model_quinto.objects.get(id=DatosAdop.persona_id)
        Datosmedicos = self.model_sexto.objects.get(id=Adop.datosMedicos_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form1' not in context:
            context['form1'] = self.segundo_form_class(instance=DocAdop)
        if 'form2' not in context:
            context['form2'] = self.tercer_form_class(instance=DatosAnim)
        if 'form3' not in context:
            context['form3'] = self.cuarto_form_class(instance=DatosAdop)
        if 'form4' not in context:
            context['form4'] = self.quinto_form_class(instance=DatosPersonaA)
        if 'form5' not in context:
            context['form5'] = self.sexto_form_class(instance=Datosmedicos)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        id_AnimalAdopcion = kwargs['pk']
        Adop = self.model.objects.get(id=id_AnimalAdopcion)
        DocAdop = self.model_segundo.objects.get(id=Adop.documentos_id)
        DatosAnim = self.model_tercero.objects.get(id=Adop.animal_id)
        DatosAdop = self.model_cuarto.objects.get(id=Adop.adoptante_id)
        DatosPersonaA = self.model_quinto.objects.get(id=DatosAdop.persona_id)
        Datosmedicos = self.model_sexto.objects.get(id=Adop.datosMedicos_id)
        form = self.form_class(request.POST, request.FILES, instance=Adop)
        form1 = self.segundo_form_class(request.POST, request.FILES, instance=DocAdop)
        form2 = self.tercer_form_class(request.POST, instance=DatosAnim)
        form3 = self.cuarto_form_class(request.POST, instance=DatosAdop)
        form4 = self.quinto_form_class(request.POST, instance=DatosPersonaA)
        form5 = self.sexto_form_class(request.POST, instance=Datosmedicos)
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            form5.save()
            form4.save()
            form3.save()
            form3.save()
            form1.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form1=form1, form2=form2, form3=form3, form4=form4, form5=form5))
'''

