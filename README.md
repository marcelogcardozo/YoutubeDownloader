
# YoutubeDownloader
<div align='center'>
    <img src="./static/assets/Screenshots%201%20-%202.png" style="width:450px">
    <img src="./static/assets/Screenshots%203%20-%204.png" style="width:450px">
</div><br>

Para utilização, acessar [aqui](https://afternoon-scrubland-71132.herokuapp.com/).<br>

# Sobre o Projeto

Este projeto foi feito para treinar o desenvolvimento de um back-end com Flask (Python) e também um pouco de front-end (flexbox, material bootstrap etc).
O projeto é basicamente um baixador de vídeos do Youtube, usando a biblioteca PyTube. Esta nos permite buscar strings na plataforma e retonar resultados, assim como
listar videos de canais e playlists.

# Motivação

A maioria dos baixadores de vídeos do Youtube é grátis, porém com diversos anúncios que atrapalham na usabilidade. Portanto, o objetivo maior é criar uma aplicação
open source e sem anúncios.

# Observações

1) A aplicação está hospedada no servidor Heroku, cujo plano grátis acabará dia 28/11/2022;
2) Para baixar vídeo na plataforma é necessário estar logado(a);
3) A segurança na parte do login não é boa, portanto, colocar e-mail e senha aleatórios, já que ambos não serão utilizados para fins de verificação.

# Próximos Passos

1) Melhoria na segurança do banco de dados/ método de login;
2) Ajustar o código para permitir o download de múltiplos vídeos (como vídeos de algum canal ou playlist);
3) Melhorias na interface
