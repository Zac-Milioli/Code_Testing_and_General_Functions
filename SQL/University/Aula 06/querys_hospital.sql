CREATE procedure IncluiPaciente
@cpf int,
@nome varchar(200),
@datanascimento date ,
@identificador_TipoConsulta int null,
@identificador_convenio int null
as

begin

    -- regra de negócio
    -- testar se o código de consulta informado existe
    if (select 1 from tipoconsulta
        where identificador = @identificador_TipoConsulta) = 0
    begin
        print 'tipo de consulta não existe'
        return  -- sai da stored procedure
    end

    -- regra de negócio
    -- testar se o cpf já existe
    if (select 1 from paciente
        where cpf = @cpf)<> 0
    begin
        print 'Paciente já cadastrado'
        return  -- sai da stored procedure
    end



    -- Inserção do paciente
    INSERT INTO Paciente (CPF, Nome, DataNascimento,
    Identificador_TipoConsulta, Identificador_Convenio)
    VALUES (@CPF, @Nome, @DataNascimento,
    @Identificador_TipoConsulta, @Identificador_Convenio);
end

create table Controle
(identificador int identity primary key,
Aud_dataHora datetime)

create procedure InsereControle
as
begin
insert into controle (aud_datahora) values (getdate())
end

create FUNCTION [dbo].[FN_DiaSemana]
(@dia INT)
RETURNS varchar(20)

as

BEGIN    

declare @cicchar varchar(20)

if @dia = 6
select @cicchar = 'Sexta-feira'
if @dia = 7    
select @cicchar = 'Sábado'
if @dia = 1
select @cicchar = 'Domingo'
if @dia = 2
select @cicchar = 'Segunda-feira'
if @dia = 3
select @cicchar = 'Terça-feira'
if @dia = 4
select @cicchar = 'Quarta-feira'
if @dia = 5
select @cicchar = 'Quinta-feira'


return @cicchar

END

EXEC IncluiPaciente
    @CPF = 12345678901,
    @Nome = 'Jorivaldo Marcio',
    @DataNascimento = '1980-05-15',
    @Identificador_TipoConsulta = 1,
    @Identificador_Convenio = 2;