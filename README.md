O objetivo deste projeto é facilitar a edição das _tags_
do Google Tag Manager criando um tipo de repositório
local na máquina do usuário.

Por enquanto o projeto suporta a edição de tags de HTML
customizado, mas é ideal que ele evolua de forma a permitir
as mesmas mudanças que a interface do GTM permite, porém
localmente no terminal do usuário. Além disso, é necessário
a exportação/importação constante dos containers na ferramenta.
Uma melhoria óbvia é fazer essa conversa pela API.

No momento, existem dois comandos

```
   gtmtoproject.py init container_name
```

Cria uma pasta chamada _project_, com um .html por tag
de HTML customizado do container.

```
   gtmproject.py compile container_name
```

Atualiza o container, refletindo as alterações nos vários
arquivos .html dentro das tags.
