# Milênio Bus - Radartona_ML
### Apresentação
Esse repositório consiste no tratamento e modelagem de dados para predição dos datasets fornecidos na Radartona, assim como todos os scripts auxiliares.

Foi desenvolvido um modelo capaz de predizer a velocidade de uma via por meio da coleta dos dados dos radares espalhados por São Paulo.

## Bases utilizadas

* base_radares
* trajetos
* OpenWeather

## Metodologia

O tratamento dos dados se deu pelo cruzamento da base **trajetos**, na qual foi possível obter os ids dos radares, datas e velocidades dos carros com **base_radares** no qual foi possível obter a velocidade limite da via, além da base **OpenWeather** na qual foi possível obter o índice de chuva em datas específicas. 

## Treinamento

O treinamento do modelo foi realizado em **python** a partir da biblioteca **sklearn**.

O treinamento é detalhado no seguinte Notebook [Jupyter de Treinamento](https://github.com/willianchan/Radartona_ML/blob/master/MachineLearning/ModeloPredi%C3%A7%C3%A3o.ipynb)

## Modelo

O modelo foi gerado e salvo em formato pickle(.pkl), podendo ser acessado pelo s3: [modelo_radartona.pkl](https://transfer-learning.s3.amazonaws.com/models/modelo_radartona.pkl?response-content-disposition=attachment&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXNhLWVhc3QtMSJGMEQCICsDjZVZzmXffsU1UGK7denn%2Bp88RcHgEIG0i%2Bye7b%2FyAiBaZq7vxuSBEz80SZPlrkugWVoRpdfae0qapgbYCXfIsyqfAgic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDE1ODgwODUzMDkxNyIM5Kamna09sHBc9LnwKvMBnZtmCuS7J4Wo7ckF2HGxIcIMrtxu%2FB693JUU7DgV89C%2F55%2F4smevkBRtxxJ2opWBYTS0o%2FcPBBYPaduxmZnI%2FdBsLYR94i1xt%2B6CsV13VW8tmRMa3HAJOkDzWW0jR7r0J85VTGaVhr8WOd99N9H65s90ZPSNSNgsvZzWppXNeboyJqCukaoliX1%2BU8OQfrkpN%2F18gjvrqWQAbod%2FSj1OdcJtcy6TI6mtdT83rqAIm3LKHlnqmo%2BJ21kkj9qQoU%2F1AdgwXpObR2he%2B89c2eil3VH8OJxjOb%2FZgGSOtxJB6EEQzQSnTshi6LfdUbkt4TLll99aMK2ByO4FOpED4zGpZwhCzIiAoH3YT9kWPiNh4bRJJOpVOo25UU%2BipVWAnwNH7uV4e79iv9Ub%2BUmeemEGLfTtP%2FVUCineEUt5R6gyo3ReObudbkS0LNa%2BwIePcXKk6YwLDJLBcyJsb%2Bq72UQTze5TilUWY3o8oTa5A1DWSqO5Ary4KLLVo2IpGsdgxdMF%2FBZIChhRQBYH5I%2Fa3YRRZHV%2FXheQaDhFeq4sM86dtu8fs95BKdVvPxQ3J7fvl3fv6o7FL%2F2YB7pzoSw50NW4aGa6u8GMncBBVkycSpLqJd%2FPsxIW%2BInlUtjS8FSTk%2FScfKKHSpHGXgS3zG%2BUlnbnELYoDNLqhnkNrn5xsyjJDeY%2FNiV4ECDSRJUMgqRLElor7qFAdNGdQbxjKQVfpQwO4kynnP9UUUhe5xJiQFOupFD9HB95ztx67fdcIX4HNOukLhy7cc9k4ZGq%2B6nvf8Fn%2FgVDV%2BiEzh9t0W8jw7mmXoqvYkieyFvs4agzHBIiYfLXxBPiPco82JgaH7hfJmEGAVR2JIh88Q73rwRxWg0%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20191118T033735Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIASJ6NZ37S5VLA3I6C%2F20191118%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=f7d962de7aa6ef232f58dcb1fe40027d5c710326583bdb7ffc5d823b66a2ee26)