const testimonialsContainer = document.querySelector('.testimonials-container')
const testimonial = document.querySelector('.testimonial')
const userImage = document.querySelector('.user-image')
const username = document.querySelector('.username')
const role = document.querySelector('.role')

const testimonials = [
    {
      name: 'Miyah Myles',
      position: 'Marketing',
      photo:
        'https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&s=707b9c33066bf8808c934c8ab394dff6',
      text:
        "He trabajado literalmente con cientos de desarrolladores de HTML/CSS y debo decir que el primer puesto es para este tipo. Este tipo es un desarrollador increíble. Hace hincapié en un código bueno y limpio y presta atención a los detalles. Me encantan los desarrolladores que respetan todos y cada uno de los aspectos de un diseño minuciosamente pensado y hacen todo lo posible para plasmarlo en código. Él va más allá y transforma ARTE en PÍXELES, sin ningún problema, cada vez.",
    },
    {
      name: 'June Cha',
      position: 'Ing. en Software',
      photo: 'https://randomuser.me/api/portraits/women/44.jpg',
      text:
        'Este tipo es un increíble desarrollador frontend que realizó la tarea exactamente como la necesitamos, hazte un favor y contrátalo, no te decepcionará el trabajo realizado. Él hará un esfuerzo adicional para asegurarse de que usted esté satisfecho con su proyecto. ¡Seguramente volveré a trabajar con él!',
    },
    {
      name: 'Iida Niskanen',
      position: 'Entrada de datos',
      photo: 'https://randomuser.me/api/portraits/women/68.jpg',
      text:
        "Este tipo es un gran trabajador. La comunicación también fue muy buena con él y fue muy receptivo en todo momento, algo que no es fácil de encontrar en muchos autónomos. Definitivamente repetiremos con él.",
    },
    {
      name: 'Renee Sims',
      position: 'Recepcionista',
      photo: 'https://randomuser.me/api/portraits/women/65.jpg',
      text:
        "Este tipo hace todo lo posible para hacer el trabajo y hacerlo bien. Es la segunda vez que lo contrato y lo volveré a contratar en el futuro.",
    },
    {
      name: 'Jonathan Nunfiez',
      position: 'Diseñador Grafico',
      photo: 'https://randomuser.me/api/portraits/men/43.jpg',
      text:
        "Me preocupaba que debido a un plazo ajustado este proyecto no se pudiera realizar. Pero este tipo me demostró que estaba equivocado, no solo entregó un trabajo sobresaliente sino que logró entregarlo 1 día antes de la fecha límite. Y cuando le pedí algunas revisiones las hizo en MINUTOS. Tengo muchas ganas de volver a trabajar con él y lo recomiendo totalmente. ¡Gracias de nuevo!",
    },
    {
      name: 'Sasha Ho',
      position: 'Contadora',
      photo:
        'https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?h=350&auto=compress&cs=tinysrgb',
      text:
        'Este tipo es un diseñador y desarrollador front-end de primer nivel. Se comunica bien, trabaja rápido y produce un trabajo de calidad. ¡Hemos tenido la suerte de trabajar con él!',
    },
    {
      name: 'Veeti Seppanen',
      position: 'Director',
      photo: 'https://randomuser.me/api/portraits/men/97.jpg',
      text:
        'Este chico es un profesional de TI joven y talentoso, proactivo y responsable, con una sólida ética de trabajo. Es muy fuerte en conversiones PSD2HTML y tecnología HTML/CSS. Aprende rápido y está ansioso por aprender nuevas tecnologías. Está enfocado y tiene buena dinámica para lograr plazos y resultados sobresalientes',
    },
  ]

let idx = 1

function updateTestimonial() {
    const { name, position, photo, text } = testimonials[idx]

    testimonial.innerHTML = text
    userImage.src = photo
    username.innerHTML = name
    role.innerHTML = position

    idx++

    if (idx > testimonials.length - 1) {
        idx = 0
    }
}

setInterval(updateTestimonial, 10000)