package io.zensoft.share.service;

import io.zensoft.share.model.PublisherServiceType;
import io.zensoft.share.model.Vacancy;
import io.zensoft.share.model.VacancyResponse;
import io.zensoft.share.service.model.VacancyResponseModelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class DefaultVacancyRetrieverService implements VacancyRetrieverService {

    private VacancyResponseModelService defaultVacancyResponseModelService;

    @Autowired
    public DefaultVacancyRetrieverService(VacancyResponseModelService defaultVacancyResponseModelService) {
        this.defaultVacancyResponseModelService = defaultVacancyResponseModelService;
    }

    @Override
    public VacancyResponse getInfo(Vacancy vacancy, PublisherServiceType publisherServiceType) {
        VacancyResponse vacancyResponse = defaultVacancyResponseModelService
            .getByVacancyUuidAndPublisherServiceType(vacancy,publisherServiceType);
        return vacancyResponse;
    }
}
