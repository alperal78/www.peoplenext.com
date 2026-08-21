// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.peoplenext.com',
  server: {
    host: '0.0.0.0',
    port: 4321
  },
  redirects: {
    '/sap-successfactors-demo/': '/demo-success-factors/',
    '/software-de-administracion-de-compensaciones/': '/successfactors-software-de-administracion-de-compensaciones/',
    '/software-de-evaluacion-de-desempeno-successfactors/': '/software-de-evaluacion-del-desempeno/',
    '/software-lms-para-empresas-successfactors/': '/software-de-e-learning-lms/',
    '/successfactors-software-de-evaluacion-de-desempeno/': '/software-de-evaluacion-del-desempeno/',
    '/planes-de-sucesion/': '/planes-de-carrera-y-desarrollo/',
    '/planes-de-sucesion-old/': '/planes-de-carrera-y-desarrollo/',
    '/software-de-reclutamiento-y-seleccion-del-personal-old/': '/software-de-reclutamiento-y-seleccion-del-personal/',
    '/recursos/ebooks/': '/recursos/',
    '/recursos/ebooks/2/': '/recursos/',
    '/recursos/ebooks/3/': '/recursos/',
    '/recursos/brochures/': '/recursos/',
    '/recursos/brochures/2/': '/recursos/',
    '/recursos/cv/': '/recursos/',
    '/recursos/hoja-de-producto/': '/recursos/',
    '/recursos/formatos/2/': '/recursos/formatos/',
    '/recursos/infografias/2/': '/recursos/infografias/',
    '/recursos/infografias/3/': '/recursos/infografias/'
  }
});

