import axios from "axios";

const baseURL = 'http://localhost:8000/api';

const apiCurso = axios.create({baseURL});

export default apiCurso;