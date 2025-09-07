






---

## Consigna 2
![punto2](../tp2/img/img-consig2.png)

### a) ¿Qué fenómeno físico se está representando en la Figura? ¿Cuáles son las características principales del mismo?

En la figura podemos ver el fenómeno de la interferencia electromagnética (también conocido como _ruido_). La interferencia es una señal eléctrica no deseada que se suma a la señal principal, y la podemos ver representada en la figura como una alteración en la propagación de la onda entre la torre y el smartphone. Los orígenes de las interferencias pueden ser internos (producidos por el propio sistema) o externas (provenientes de dispositivos ajenos) que es el caso de la figura, en ella podemos ver que un taladro mecánico produce la interferencia. 
Las principales características de la interferencia son:
- Superposición de ondas: La base de la interferencia es el principio de superposición, cuando dos o más ondas electromagnéticas coinciden en el espacio y tiempo, sus campos eléctricos y magnéticos se suman. Esto puede producir zonas de refuerzo (constructiva) o de cancelación (destructiva). En la práctica suele haber una combinación de ambas.
- La interferencia depende de la frecuencia de onda.
- Ondas con la misma frecuencia pueden interferir más fácilmente, por ejemplo dos routers en el mismo canal de 2.4 GHz.
- Puede ser constante en el tiempo si las fuentes son coherentes, como dos láseres con la misma frecuencia estable.
- O variable/aleatoria si las fuentes son incoherentes, como ruidos eléctricos.

### b) Recordando las bandas de transmisión vistas en el TP01, investigar: ¿A qué tipos de transmisión afecta este fenómeno? ¿Cuáles son más resilientes al mismo?

Las transmisiones que operan en bandas de alta frecuencia son las más vulnerables al ruido, ya que presentan una mayor sensibilidad frente a obstáculos físicos y condiciones atmosféricas. Por ejemplo, hoy en día es normal que los ISP ofrezcan routers con dos bandas de frecuencias Wi-Fi, una de 5 GHz la cuál tiene la ventaja de ser más rápida pero es muy susceptible a las interferencias y obstáculos físicos. Y la otra señal que ofrece está en una banda de frecuencia más baja (2.4 GHz) pero es más resistente a las interferencias. 

### c) ¿Qué es la SNR? ¿Tiene algo que ver con el concepto de BER que vimos en el TP01?

La SNR (_Signal-to-Noise Ratio_) es una medida que compara la potencia de la señal útil con respecto a la potencia del ruido presente en el mismo canal o medio de transmisión.
- Un mayor SNR significa una señal más fuerte en relación al ruido, lo que implica una mejor calidad en la transmición de la señal.
El BER (Bit-Error-Rate) es la tasa de error de bits, es decir, la proporción de bits transmitidos que se reciben de forma incorrecta debido a interferencias.
- A medida que disminuye el SNR el BER aumenta lo que significa que más bits se reciben de manera errónea.

