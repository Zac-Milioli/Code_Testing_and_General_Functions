USE HospitalSaude;

-- Listar todos os pacientes com suas respectivas consultas e situações.
SELECT * FROM Paciente 
INNER JOIN Consulta ON Paciente.Identificador = Consulta.Identificador_Paciente
INNER JOIN SituacaoConsulta ON Consulta.Identificador_TipoConsulta = SituacaoConsulta.Identificador;

-- Encontrar todos os profissionais da especialidade Endocrinologia
SELECT * FROM Profissional INNER JOIN Especialidade
ON Profissional.Identificador_Especialidade = Especialidade.Identificador
WHERE Especialidade.Descricao = 'Endocrinologia';

-- Contar o número de consultas por tipo de consulta para o mês 5
SELECT COUNT(*) AS 'Contagem', TipoConsulta.Descricao FROM TipoConsulta
INNER JOIN Paciente ON Paciente.Identificador = TipoConsulta.Identificador
INNER JOIN Servico ON Servico.Identificador_Paciente = Paciente.Identificador
WHERE MONTH(Servico.DataHora) = 5
GROUP BY (TipoConsulta.Descricao);

-- Listar os serviços realizados por cada profissional, incluindo a descrição do tipo de serviço.
SELECT * FROM Profissional
INNER JOIN Especialidade
ON Profissional.Identificador_Especialidade = Especialidade.Identificador

-- Identificar pacientes que não têm convênio.
SELECT * FROM Paciente
LEFT JOIN Convenio
ON Convenio.Identificador = Paciente.Identificador
WHERE Convenio.Identificador IS NULL;

-- Listar todas as consultas agendadas para o Dr. João Silva, incluindo o nome do paciente, o profissional e a especialidade.
SELECT * FROM Profissional
INNER JOIN Especialidade ON Profissional.Identificador_Especialidade = Especialidade.Identificador
INNER JOIN Consulta ON Consulta.Identificador_Profissional = Profissional.Identificador
INNER JOIN Paciente ON Paciente.Identificador = Consulta.Identificador_Paciente
WHERE Profissional.Nome = 'Dr. João Silva';

-- Encontrar o número de consultas em cada situação (por exemplo, agendada, realizada, cancelada)
SELECT COUNT(*) AS 'Quantidade', SituacaoConsulta.Descricao FROM Consulta
INNER JOIN SituacaoConsulta ON SituacaoConsulta.Identificador = Consulta.Identificador_Situacao
GROUP BY (SituacaoConsulta.Descricao);

