import csv

# Datos de ejemplo de correos electrónicos
datos_correos = [
    {"Asunto": "Reunión de equipo", "Remitente": "juan@example.com", "Destinatario": "maria@example.com", "Mensaje": "Hola María, ¿podemos reunirnos mañana para discutir el proyecto?"},
    {"Asunto": "Confirmación de reserva", "Remitente": "reservas@hotel.com", "Destinatario": "cliente@example.com", "Mensaje": "Estimado cliente, su reserva para el 15 de marzo ha sido confirmada."},
    {"Asunto": "Solicitud de información", "Remitente": "info@empresa.com", "Destinatario": "ventas@empresa.com", "Mensaje": "Hola, ¿podrían proporcionarme más información sobre sus productos?"},
    {"Asunto": "Oferta de empleo", "Remitente": "rrhh@empresa.com", "Destinatario": "candidato@example.com", "Mensaje": "Estimado candidato, estamos interesados en su perfil para un puesto en nuestra empresa."},
    {"Asunto": "Invitación a evento", "Remitente": "evento@organizacion.com", "Destinatario": "asistente@example.com", "Mensaje": "Hola, te invitamos cordialmente a nuestro evento de lanzamiento."},
    {"Asunto": "Aviso de pago pendiente", "Remitente": "facturacion@empresa.com", "Destinatario": "cliente@example.com", "Mensaje": "Le recordamos que tiene un pago pendiente por la factura número 12345."},
    {"Asunto": "Confirmación de suscripción", "Remitente": "newsletter@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Gracias por suscribirte a nuestro boletín de noticias."},
    {"Asunto": "Recordatorio de reunión", "Remitente": "organizador@empresa.com", "Destinatario": "participante@example.com", "Mensaje": "Este es un recordatorio para la reunión programada para mañana."},
    {"Asunto": "Respuesta a consulta", "Remitente": "soporte@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Hemos recibido su consulta y nos pondremos en contacto con usted lo antes posible."},
    {"Asunto": "Feliz cumpleaños", "Remitente": "equipo@empresa.com", "Destinatario": "empleado@example.com", "Mensaje": "¡Feliz cumpleaños! Esperamos que tengas un día maravilloso."},
    {"Asunto": "Recordatorio de cita médica", "Remitente": "clinica@example.com", "Destinatario": "paciente@example.com", "Mensaje": "Estimado paciente, le recordamos su cita médica para el próximo lunes a las 10:00 AM."},
    {"Asunto": "Confirmación de compra", "Remitente": "ventas@tienda.com", "Destinatario": "cliente@example.com", "Mensaje": "Gracias por tu compra. Tu pedido ha sido confirmado y será enviado pronto."},
    {"Asunto": "Notificación de entrega", "Remitente": "logistica@empresa.com", "Destinatario": "cliente@example.com", "Mensaje": "Su paquete ha sido entregado. Por favor, confirme la recepción."},
    {"Asunto": "Respuesta a solicitud de soporte", "Remitente": "soporte@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Hemos recibido su solicitud de soporte y estamos trabajando en resolver su problema."},
    {"Asunto": "Invitación a participar en encuesta", "Remitente": "encuestas@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Hola, nos gustaría conocer tu opinión. ¿Podrías participar en nuestra encuesta rápida?"},
    {"Asunto": "Aviso de renovación de membresía", "Remitente": "membresias@club.com", "Destinatario": "socio@example.com", "Mensaje": "Su membresía está a punto de vencer. Renueve ahora para seguir disfrutando de los beneficios."},
    {"Asunto": "Confirmación de reserva de vuelo", "Remitente": "reservas@aerolinea.com", "Destinatario": "pasajero@example.com", "Mensaje": "Su reserva de vuelo ha sido confirmada. Adjunto encontrará los detalles de su itinerario."},
    {"Asunto": "Notificación de cambio de contraseña", "Remitente": "seguridad@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Se ha cambiado su contraseña. Si no fue usted, por favor contáctenos de inmediato."},
    {"Asunto": "Aviso de suspensión de servicio", "Remitente": "servicio@empresa.com", "Destinatario": "cliente@example.com", "Mensaje": "Le informamos que su servicio será suspendido temporalmente por mantenimiento programado."},
    {"Asunto": "Confirmación de inscripción", "Remitente": "inscripciones@evento.com", "Destinatario": "participante@example.com", "Mensaje": "¡Felicidades! Su inscripción para el evento ha sido confirmada."},
    {"Asunto": "Solicitud de cotización", "Remitente": "cotizaciones@empresa.com", "Destinatario": "proveedor@example.com", "Mensaje": "Estimado proveedor, por favor envíe una cotización para los productos solicitados."},
    {"Asunto": "Confirmación de suscripción al boletín", "Remitente": "boletin@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Gracias por suscribirte a nuestro boletín informativo. Esperamos que disfrutes de nuestras noticias y ofertas."},
    {"Asunto": "Recordatorio de pago de factura", "Remitente": "facturacion@empresa.com", "Destinatario": "cliente@example.com", "Mensaje": "Le recordamos que su factura vence hoy. Por favor, realice el pago antes de la fecha de vencimiento."},
    {"Asunto": "Invitación a evento de networking", "Remitente": "networking@empresa.com", "Destinatario": "participante@example.com", "Mensaje": "Te invitamos a nuestro evento de networking donde podrás conocer a otros profesionales y expandir tu red de contactos."},
    {"Asunto": "Aviso de actualización de términos de servicio", "Remitente": "legal@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "Hemos actualizado nuestros términos de servicio. Por favor, revisa los cambios y acepta para continuar utilizando nuestros servicios."},
    {"Asunto": "Confirmación de reserva de sala de reuniones", "Remitente": "reservas@empresa.com", "Destinatario": "empleado@example.com", "Mensaje": "Su reserva de sala de reuniones para mañana ha sido confirmada."},
    {"Asunto": "Aviso de entrega retrasada", "Remitente": "logistica@empresa.com", "Destinatario": "cliente@example.com", "Mensaje": "Lamentamos informarle que su entrega se retrasará debido a problemas logísticos. Estamos trabajando para resolverlo lo antes posible."},
    {"Asunto": "Invitación a participar en encuesta de satisfacción", "Remitente": "encuestas@empresa.com", "Destinatario": "usuario@example.com", "Mensaje": "¡Queremos escuchar tu opinión! Por favor, participa en nuestra encuesta de satisfacción para mejorar nuestros servicios."},
    {"Asunto": "Aviso de cambio de horario", "Remitente": "horarios@empresa.com", "Destinatario": "empleado@example.com", "Mensaje": "Le informamos que a partir del próximo mes, el horario de trabajo se modificará. Por favor, revise el nuevo horario adjunto."},
    {"Asunto": "Solicitud de información sobre empleo", "Remitente": "empleo@empresa.com", "Destinatario": "reclutamiento@example.com", "Mensaje": "Estimado equipo de reclutamiento, estoy interesado en conocer las oportunidades de empleo disponibles en su empresa."},
]

# Nombre del archivo CSV
nombre_archivo = "ejemplo_correos.csv"

# Escribir los datos en el archivo CSV
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    campos = ["Asunto", "Remitente", "Destinatario", "Mensaje"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor_csv.writeheader()
    for correo in datos_correos:
        escritor_csv.writerow(correo)

print(f"Se ha generado el archivo '{nombre_archivo}' con éxito.")